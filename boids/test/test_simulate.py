from boids.boids import simulate
from matplotlib import pyplot as plt
from matplotlib import animation
from mock import patch
from nose.tools import assert_equal
import yaml
import os

@patch("matplotlib.pyplot.axes")
@patch("matplotlib.animation.FuncAnimation")
def test_simulate(mock_FuncAnimation, mock_axes):
    yaml.load(open(os.path.join(os.path.dirname(__file__),'fixtures/test_params.yaml'))
    boids = ([0], [0], [0], [0])
    simulate(test_params, boids, False)
    mock_axes.assert_called_with(
        xlim=(
            test_params["axes_min"], test_params["axes_max"]), ylim=(
            test_params["axes_min"], test_params["axes_max"]))
    args = mock_FuncAnimation.call_args
    assert_equal(args[1]['frames'], test_params["number_of_frames"])
    assert_equal(args[1]['interval'], test_params["frame_delay"])
