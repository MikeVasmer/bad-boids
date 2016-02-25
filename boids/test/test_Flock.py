from nose.tools import assert_equal, assert_almost_equal
from boids.boids import Flock
import yaml
import os
from mock import patch

test_params = yaml.load(
    open(
        os.path.join(
            os.path.dirname(__file__),
            'fixtures/test_params.yaml')))
boid_limits = test_params["boid_params"]
flock_params = test_params["flock_params"]

# Mock Boid so that errors in the Boid class don't cause this test to fail


@patch("boids.boids.Boid")
def test_init(mock_Boid):
    test_flock = Flock(flock_params, boid_limits)
    assert_equal(sum(len(x)
                     for x in test_flock.positions), flock_params["number_of_boids"] * 2)
    assert_equal(sum(len(x)
                     for x in test_flock.velocities), flock_params["number_of_boids"] * 2)
