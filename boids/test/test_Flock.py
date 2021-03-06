from nose.tools import assert_equal, assert_almost_equal
from boids.model import Flock
import yaml
import os
from mock import patch
import numpy as np

test_params = yaml.load(
    open(
        os.path.join(
            os.path.dirname(__file__),
            'fixtures/test_params.yaml')))
boid_limits = test_params["boid_params"]
flock_params = test_params["flock_params"]
test_flock = Flock(flock_params, boid_limits)

# Mock Boid so that errors in the Boid class don't cause this test to fail


@patch("boids.model.Boid")
def test_init(mock_Boid):
    assert_equal(sum(len(x)
                     for x in test_flock.positions), flock_params["number_of_boids"] * 2)
    assert_equal(sum(len(x)
                     for x in test_flock.velocities), flock_params["number_of_boids"] * 2)


def test_move_to_middle():
    test_data = yaml.load(
        open(
            os.path.join(
                os.path.dirname(__file__),
                'fixtures/move_middle_fixture.yaml')))
    test_flock.positions[0] = test_data["before"][0][0]
    test_flock.positions[1] = test_data["before"][0][1]
    test_flock.velocities[0] = test_data["before"][1][0]
    test_flock.velocities[1] = test_data["before"][1][1]
    test_flock.move_to_middle()
    np.testing.assert_allclose(
        test_data["after"][0],
        test_flock.positions.tolist(), rtol=test_params["delta"])
    np.testing.assert_allclose(
        test_data["after"][1],
        test_flock.velocities.tolist(), rtol=test_params["delta"])


def test_fly_away_nearby():
    test_data = yaml.load(
        open(
            os.path.join(
                os.path.dirname(__file__),
                'fixtures/fly_away_fixture.yaml')))
    test_flock.positions[0] = test_data["before"][0][0]
    test_flock.positions[1] = test_data["before"][0][1]
    test_flock.velocities[0] = test_data["before"][1][0]
    test_flock.velocities[1] = test_data["before"][1][1]
    separations = test_flock.positions[
        :, np.newaxis, :] - test_flock.positions[:, :, np.newaxis]
    square_distances = np.sum(separations * separations, 0)
    test_flock.fly_away_nearby(separations, square_distances)
    np.testing.assert_allclose(
        test_data["after"][0],
        test_flock.positions.tolist(), rtol=test_params["delta"])
    np.testing.assert_allclose(
        test_data["after"][1],
        test_flock.velocities.tolist(), rtol=test_params["delta"])


def test_match_boids_speeds():
    test_data = yaml.load(
        open(
            os.path.join(
                os.path.dirname(__file__),
                'fixtures/match_fixture.yaml')))
    test_flock.positions[0] = test_data["before"][0][0]
    test_flock.positions[1] = test_data["before"][0][1]
    test_flock.velocities[0] = test_data["before"][1][0]
    test_flock.velocities[1] = test_data["before"][1][1]
    separations = test_flock.positions[
        :, np.newaxis, :] - test_flock.positions[:, :, np.newaxis]
    square_distances = np.sum(separations * separations, 0)
    test_flock.match_boids_speed(square_distances)
    np.testing.assert_allclose(
        test_data["after"][0],
        test_flock.positions.tolist(), rtol=test_params["delta"])
    np.testing.assert_allclose(
        test_data["after"][1],
        test_flock.velocities.tolist(), rtol=test_params["delta"])


def test_update_boids():
    test_data = yaml.load(
        open(
            os.path.join(
                os.path.dirname(__file__),
                'fixtures/update_boids_fixture.yaml')))
    test_flock.positions[0] = test_data["before"][0][0]
    test_flock.positions[1] = test_data["before"][0][1]
    test_flock.velocities[0] = test_data["before"][1][0]
    test_flock.velocities[1] = test_data["before"][1][1]
    test_flock.update_boids()
    np.testing.assert_allclose(
        test_data["after"][0],
        test_flock.positions.tolist(), rtol=test_params["delta"])
    np.testing.assert_allclose(
        test_data["after"][1],
        test_flock.velocities.tolist(), rtol=test_params["delta"])
