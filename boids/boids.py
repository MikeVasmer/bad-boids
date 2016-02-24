"""
A deliberately bad implementation of [Boids](http://dl.acm.org/citation.cfm?doid=37401.37406)
for use as an exercise on refactoring.
"""

from matplotlib import pyplot as plt
from matplotlib import animation
import random
import yaml
import os
import inspect

# Deliberately terrible code for teaching purposes

fixture_path = os.path.dirname(os.path.abspath(inspect.stack()[0][1])) + "/fixtures/params.yaml"
params = yaml.load(open(fixture_path))
number_of_boids = params["number_of_boids"]
boid_limits = params["boid_limits"]

class Boid(object):
    def __init__(self, boid_limits):
		self.position = (random.uniform(boid_limits["min_x_position"],boid_limits["max_x_position"]), random.uniform(boid_limits["min_y_position"],boid_limits["max_y_position"]))
		self.velocity = (random.uniform(boid_limits["min_x_velocity"],boid_limits["max_x_velocity"]), random.uniform(boid_limits["min_y_velocity"],boid_limits["max_y_velocity"]))

boids = ([0]*number_of_boids, [0]*number_of_boids, [0]*number_of_boids, [0]*number_of_boids)
for x in range(number_of_boids):
	boid = Boid(boid_limits)
	boids[0][x] = boid.position[0]
	boids[1][x] = boid.position[1]
	boids[2][x] = boid.velocity[0]
	boids[2][x] = boid.velocity[1]

def update_boids(boids):
	xs,ys,xvs,yvs=boids
	# Fly towards the middle
	move_middle_strength = params["move_middle_strength"]
	for i in range(len(xs)):
		for j in range(len(xs)):
			xvs[i]=xvs[i]+(xs[j]-xs[i])*move_middle_strength/len(xs)
	for i in range(len(xs)):
		for j in range(len(xs)):
			yvs[i]=yvs[i]+(ys[j]-ys[i])*move_middle_strength/len(xs)
	# Fly away from nearby boids
	for i in range(len(xs)):
		for j in range(len(xs)):
			if (xs[j]-xs[i])**2 + (ys[j]-ys[i])**2 < params["min_separation_squared"]:
				xvs[i]=xvs[i]+(xs[i]-xs[j])
				yvs[i]=yvs[i]+(ys[i]-ys[j])
	# Try to match speed with nearby boids
	matching_strength = params["matching_strength"]
	for i in range(len(xs)):
		for j in range(len(xs)):
			if (xs[j]-xs[i])**2 + (ys[j]-ys[i])**2 < params["nearby_distance_squared"]:
				xvs[i]=xvs[i]+(xvs[j]-xvs[i])*matching_strength/len(xs)
				yvs[i]=yvs[i]+(yvs[j]-yvs[i])*matching_strength/len(xs)
	# Move according to velocities
	for i in range(len(xs)):
		xs[i]=xs[i]+xvs[i]
		ys[i]=ys[i]+yvs[i]

def simulate(params, boids, show=True):
	axes_min, axes_max = params["axes_min"], params["axes_max"]
	figure = plt.figure()
	axes = plt.axes(xlim=(axes_min,axes_max), ylim=(axes_min,axes_max))
	scatter = axes.scatter(boids[0],boids[1])
	def animate(frame):
	   update_boids(boids)
	   scatter.set_offsets(zip(boids[0],boids[1]))
	anim = animation.FuncAnimation(figure, animate, frames=params["number_of_frames"], interval=params["frame_delay"])
	if show:
		plt.show()

if __name__ == "__main__":
    simulate(params,boids)
