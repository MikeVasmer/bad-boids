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

if __name__ == "__main__":
    # Load parameters from fixture file
    params = yaml.load(
        open(
            os.path.join(
                os.path.dirname(__file__),
                'fixtures/params.yaml')))
    flock_params = params["flock_params"]
    boid_params = params["boid_params"]
    anim_params = params["anim_params"]

    flock = Flock(flock_params, boid_params)
    simulate(anim_params, flock)
