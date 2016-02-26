from boids.boids import Boid
import yaml
import os
from nose.tools import assert_true

def test_init():
    test_params = yaml.load(
        open(
            os.path.join(
                os.path.dirname(__file__),
                'fixtures/test_params.yaml')))
    boid_limits = test_params["boid_params"]
    # Run the test a few times to make sure an error is detected
    for i in range(test_params["test_iterations"]):
        test_boid = Boid(boid_limits)
        assert_true(boid_limits["min_x_position"] <= test_boid.position[0] <= boid_limits["max_x_position"])
        assert_true(boid_limits["min_y_position"] <= test_boid.position[1] <= boid_limits["max_y_position"])
        assert_true(boid_limits["min_x_velocity"] <= test_boid.velocity[0] <= boid_limits["max_x_velocity"])
        assert_true(boid_limits["min_y_velocity"] <= test_boid.velocity[1] <= boid_limits["max_y_velocity"])
