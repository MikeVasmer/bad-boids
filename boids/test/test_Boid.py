from nose.tools import assert_equal
from boids.boids import Boid
import random
import yaml
import os
from mock import call, patch

@patch("random.uniform")
def test_Boid(mock_random_uniform):
    test_params = yaml.load(open(os.path.join(os.path.dirname(__file__),'fixtures/test_params.yaml')))
    boid_limits = test_params["boid_limits"]
    test_boid = Boid(boid_limits)
    calls = [call(boid_limits["min_x_position"],boid_limits["max_x_position"]), call(boid_limits["min_y_position"],boid_limits["max_y_position"]), call(boid_limits["min_x_velocity"],boid_limits["max_x_velocity"]), call(boid_limits["min_y_velocity"],boid_limits["max_y_velocity"])]
    mock_random_uniform.assert_has_calls(calls)
