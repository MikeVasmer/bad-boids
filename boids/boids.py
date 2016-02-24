"""
A deliberately bad implementation of [Boids](http://dl.acm.org/citation.cfm?doid=37401.37406)
for use as an exercise on refactoring.
"""

from matplotlib import pyplot as plt
from matplotlib import animation
import random
import yaml

# Deliberately terrible code for teaching purposes

min_x_position, max_x_position = -450, 50
min_y_position, max_y_position = 300, 600
min_x_velocity, max_x_velocity = 0, 10
min_y_velocity, max_y_velocity = -20, 20
number_of_boids = 50

class Boid(object):
    def __init__(self, min_x_position, max_x_position, min_y_position, max_y_position, min_x_velocity, max_x_velocity, min_y_velocity, max_y_velocity):
		self.position = (random.uniform(min_x_position,max_x_position), random.uniform(min_y_position,max_y_position))
		self.velocity = (random.uniform(min_x_velocity,max_x_velocity), random.uniform(min_y_velocity,max_y_velocity))

boids = ([0]*number_of_boids, [0]*number_of_boids, [0]*number_of_boids, [0]*number_of_boids)
for x in range(number_of_boids):
	boid = Boid(min_x_position, max_x_position, min_y_position, max_y_position, min_x_velocity, max_x_velocity, min_y_velocity, max_y_velocity)
	boids[0][x] = boid.position[0]
	boids[1][x] = boid.position[1]
	boids[2][x] = boid.velocity[0]
	boids[2][x] = boid.velocity[1]

def update_boids(boids):
	xs,ys,xvs,yvs=boids
	# Fly towards the middle
	move_middle_strength = 0.01
	for i in range(len(xs)):
		for j in range(len(xs)):
			xvs[i]=xvs[i]+(xs[j]-xs[i])*move_middle_strength/len(xs)
	for i in range(len(xs)):
		for j in range(len(xs)):
			yvs[i]=yvs[i]+(ys[j]-ys[i])*move_middle_strength/len(xs)
	# Fly away from nearby boids
	min_separation_squared = 100
	for i in range(len(xs)):
		for j in range(len(xs)):
			if (xs[j]-xs[i])**2 + (ys[j]-ys[i])**2 < min_separation_squared:
				xvs[i]=xvs[i]+(xs[i]-xs[j])
				yvs[i]=yvs[i]+(ys[i]-ys[j])
	# Try to match speed with nearby boids
	nearby_distance_squared = 10000
	matching_strength = 0.125
	for i in range(len(xs)):
		for j in range(len(xs)):
			if (xs[j]-xs[i])**2 + (ys[j]-ys[i])**2 < nearby_distance_squared:
				xvs[i]=xvs[i]+(xvs[j]-xvs[i])*matching_strength/len(xs)
				yvs[i]=yvs[i]+(yvs[j]-yvs[i])*matching_strength/len(xs)
	# Move according to velocities
	for i in range(len(xs)):
		xs[i]=xs[i]+xvs[i]
		ys[i]=ys[i]+yvs[i]

axes_min, axes_max = -500, 1500
number_of_frames, frame_delay = 50, 50

def simulate(axes_min, axes_max, number_of_frames, frame_delay, boids, show=True):
	figure = plt.figure()
	axes = plt.axes(xlim=(axes_min,axes_max), ylim=(axes_min,axes_max))
	scatter = axes.scatter(boids[0],boids[1])
	def animate(frame):
	   update_boids(boids)
	   scatter.set_offsets(zip(boids[0],boids[1]))
	anim = animation.FuncAnimation(figure, animate, frames=number_of_frames, interval=frame_delay)
	if show:
		plt.show()

if __name__ == "__main__":
    simulate(axes_min,axes_max,number_of_frames,frame_delay,boids)
