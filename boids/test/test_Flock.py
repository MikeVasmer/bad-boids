from nose.tools import assert_equal
from boids.boids import Flock
import yaml
import os
from mock import patch

test_params = yaml.load(open(os.path.join(os.path.dirname(__file__),'fixtures/test_params.yaml')))
boid_limits = test_params["boid_limits"]
number_of_boids = test_params["number_of_boids"]

#Mock Boid so that errors in the Boid class don't cause this test to fail
@patch("boids.boids.Boid")
def test_init(mock_Boid):
    test_flock = Flock(number_of_boids, boid_limits)
    assert_equal(len(test_flock.boids), number_of_boids)

@patch("boids.boids.Boid")
def test_boids_to_tuple(mock_Boid):
    test_flock = Flock(number_of_boids, boid_limits)
    test_tuple = test_flock.boids_to_tuple()
    assert_equal(sum(len(x) for x in test_tuple), number_of_boids*4)
