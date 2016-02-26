"""
A deliberately bad implementation of [Boids](http://dl.acm.org/citation.cfm?doid=37401.37406)
for use as an exercise on refactoring.
"""

from matplotlib import pyplot as plt
from matplotlib import animation
import random
import yaml
import os
import numpy as np

class Boid(object):
    def __init__(self, boid_params):
        self.position = (random.uniform(boid_params["min_x_position"],boid_params["max_x_position"]), random.uniform(boid_params["min_y_position"],boid_params["max_y_position"]))
        self.velocity = (random.uniform(boid_params["min_x_velocity"],boid_params["max_x_velocity"]), random.uniform(boid_params["min_y_velocity"],boid_params["max_y_velocity"]))

class Flock(object):
    def __init__(self, flock_params, boid_params):
        self.boid_params = boid_params
        self.flock_params = flock_params
        self.number_of_boids = flock_params["number_of_boids"]
        self.positions = np.zeros((2, self.number_of_boids))
        self.velocities = np.zeros((2, self.number_of_boids))
        for x in range(self.number_of_boids):
            boid = Boid(boid_params)
            self.positions[0][x] = boid.position[0]
            self.positions[1][x] = boid.position[1]
            self.velocities[0][x] = boid.velocity[0]
            self.velocities[1][x] = boid.velocity[1]

    def move_to_middle(self):
        # Preferentially set boids to fly towards the middle of the flock
        move_middle_strength = self.flock_params["move_middle_strength"]
        middle = np.mean(self.positions, 1)
        direction_to_middle = self.positions - middle[:,np.newaxis]
        self.velocities -= direction_to_middle * move_middle_strength

    def fly_away_nearby(self, separations, square_distances):
        # Fly away from nearby boids
        far_away = square_distances > self.flock_params["min_separation_squared"]
        separations_if_close = np.copy(separations)
        separations_if_close[0,:,:][far_away] = 0
        separations_if_close[1,:,:][far_away] = 0
        self.velocities += np.sum(separations_if_close,1)

    def match_boids_speed(self, square_distances):
        # Match speed with nearby boids
        matching_strength = self.flock_params["matching_strength"]
        velocity_differences = self.velocities[:,np.newaxis,:] - self.velocities[:,:,np.newaxis]
        very_far = square_distances > self.flock_params["nearby_distance_squared"]
        velocity_differences_if_close = np.copy(velocity_differences)
        velocity_differences_if_close[0,:,:][very_far] =0
        velocity_differences_if_close[1,:,:][very_far] =0
        self.velocities -= np.mean(velocity_differences_if_close, 1) * self.flock_params["matching_strength"]

    def update_boids(self):
        separations = self.positions[:,np.newaxis,:] - self.positions[:,:,np.newaxis]
        squared_displacements = separations * separations
        square_distances = np.sum(squared_displacements, 0)
        self.move_to_middle()
        self.fly_away_nearby(separations, square_distances)
        self.match_boids_speed(square_distances)
    	# Move according to velocities
    	self.positions += self.velocities

def simulate(params, flock, show=True):
	axes_min, axes_max = params["axes_min"], params["axes_max"]
	figure = plt.figure()
	axes = plt.axes(xlim=(axes_min,axes_max), ylim=(axes_min,axes_max))
	scatter = axes.scatter(flock.positions[0], flock.positions[1])
	def animate(frame):
	   flock.update_boids()
	   scatter.set_offsets(zip(flock.positions[0], flock.positions[1]))
	anim = animation.FuncAnimation(figure, animate, frames=params["number_of_frames"], interval=params["frame_delay"])
	if show:
		plt.show()

if __name__ == "__main__":
    #Load parameters from fixture file
    params = yaml.load(open(os.path.join(os.path.dirname(__file__),'fixtures/params.yaml')))
    flock_params = params["flock_params"]
    boid_params = params["boid_params"]
    anim_params = params["anim_params"]

    flock = Flock(flock_params, boid_params)
    simulate(anim_params, flock)
