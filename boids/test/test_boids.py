from boids.boids import simulate, Flock
from nose.tools import assert_almost_equal
import os
import yaml


def test_bad_boids_regression():
    regression_data = yaml.load(
        open(
            os.path.join(
                os.path.dirname(__file__),
                'fixtures/fixture.yml')))
    test_params = yaml.load(
        open(
            os.path.join(
                os.path.dirname(__file__),
                'fixtures/test_params.yaml')))
    test_flock = Flock(
        test_params["number_of_boids"],
        test_params["boid_limits"])
    test_flock.positions[0] = regression_data["before"][0]
    test_flock.positions[1] = regression_data["before"][1]
    test_flock.velocities[0] = regression_data["before"][2]
    test_flock.velocities[1] = regression_data["before"][3]
    test_flock.update_boids()
    for after, before in zip(
            regression_data["after"], test_flock.positions + test_flock.velocities):
        for after_value, before_value in zip(after, before):
            assert_almost_equal(after_value, before_value, delta=0.01)
