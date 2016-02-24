from nose.tools import assert_equal
from boids.boids import Boid
import random
import yaml
import os
import inspect
from mock import call, patch

@patch("random.uniform")
def test_Boid(mock_random_uniform):
    fixture_path = os.path.dirname(os.path.abspath(inspect.stack()[0][1])) + "/fixtures/test_params.yaml"
    test_params = yaml.load(open(fixture_path))
    boid_limits = test_params["boid_limits"]
    test_boid = Boid(boid_limits)
    calls = [call(boid_limits["min_x_position"],boid_limits["max_x_position"]), call(boid_limits["min_y_position"],boid_limits["max_y_position"]), call(boid_limits["min_x_velocity"],boid_limits["max_x_velocity"]), call(boid_limits["min_y_velocity"],boid_limits["max_y_velocity"])]
    mock_random_uniform.assert_has_calls(calls)
