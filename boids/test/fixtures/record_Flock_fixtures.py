import yaml
from boids.boids import Flock
import os
from copy import deepcopy
import numpy as np

test_params = yaml.load(
    open(
        os.path.join(
            os.path.dirname(__file__),
            'test_params.yaml')))
test_flock = Flock(
    test_params["flock_params"],
    test_params["boid_params"])

def record_move_middle_fixture():
    before = deepcopy([test_flock.positions.tolist(), test_flock.velocities.tolist()])
    test_flock.move_to_middle()
    after = [test_flock.positions.tolist(), test_flock.velocities.tolist()]
    fixture = {"before" : before, "after" : after}
    with open(os.path.join(
        os.path.dirname(__file__),
        'move_middle_fixture.yaml'), "w") as f:
        f.write(yaml.dump(fixture))

def record_fly_away_fixture():
    before = deepcopy([test_flock.positions.tolist(), test_flock.velocities.tolist()])
    test_flock.fly_away_nearby()
    after = [test_flock.positions.tolist(), test_flock.velocities.tolist()]
    fixture = {"before" : before, "after" : after}
    with open(os.path.join(
        os.path.dirname(__file__),
        'fly_away_fixture.yaml'), "w") as f:
        f.write(yaml.dump(fixture))

if __name__ == "__main__":
    #record_move_middle_fixture()
    #record_fly_away_fixture()
