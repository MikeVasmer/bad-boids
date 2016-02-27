from argparse import ArgumentParser
from simulate import simulate
from model import Flock
import yaml
import os


def process():
    parser = ArgumentParser(
        description="Simulate the flocking behaviour of a number of birds. When no configuration file is given the simulation will run with default parameters and an example configuration file (containing the default parameters) will be saved in the current directory.")
    parser.add_argument("--file", "-f",
                        help="The configuration file, in yaml format")

    arguments = parser.parse_args()

    if arguments.file:
        params = yaml.load(open(arguments.file))
    else:
        params = yaml.load(
            open(
                os.path.join(
                    os.path.dirname(__file__),
                    'params.yaml')))
        with open('example_config.yaml', "w") as f:
            f.write(yaml.dump(params))

    flock_params = params["flock_params"]
    boid_params = params["boid_params"]
    anim_params = params["anim_params"]
    flock = Flock(flock_params, boid_params)
    simulate(anim_params, flock)

if __name__ == "__main__":
    process()
