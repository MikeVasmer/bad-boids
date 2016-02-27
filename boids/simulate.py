from matplotlib import pyplot as plt
from matplotlib import animation
from model import Flock
import yaml
import os


def simulate(params, flock, show=True):
    axes_min, axes_max = params["axes_min"], params["axes_max"]
    figure = plt.figure()
    axes = plt.axes(xlim=(axes_min, axes_max), ylim=(axes_min, axes_max))
    scatter = axes.scatter(flock.positions[0], flock.positions[1])

    def animate(frame):
        flock.update_boids()
        scatter.set_offsets(zip(flock.positions[0], flock.positions[1]))

    anim = animation.FuncAnimation(
        figure,
        animate,
        frames=params["number_of_frames"],
        interval=params["frame_delay"])
    if show:
        plt.show()
