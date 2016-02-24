from boids.boids import simulate
from matplotlib import pyplot as plt
from matplotlib import animation
from mock import patch
from nose.tools import assert_equal


@patch("matplotlib.pyplot.axes")
@patch("matplotlib.animation.FuncAnimation")
def test_simulate(mock_FuncAnimation, mock_axes):
    params = {"number_of_frames" : 40, "frame_delay" : 55, "axes_min" : -600, "axes_max" : 1600}
    boids = ([0], [0], [0], [0])
    simulate(params, boids, False)
    mock_axes.assert_called_with(
        xlim=(
            params["axes_min"], params["axes_max"]), ylim=(
            params["axes_min"], params["axes_max"]))
    args = mock_FuncAnimation.call_args
    assert_equal(args[1]['frames'], params["number_of_frames"])
    assert_equal(args[1]['interval'], params["frame_delay"])
