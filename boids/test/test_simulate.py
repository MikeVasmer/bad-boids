from boids.boids import simulate
from matplotlib import pyplot as plt
from matplotlib import animation
from mock import patch
from nose.tools import assert_equal


@patch("matplotlib.pyplot.axes")
@patch("matplotlib.animation.FuncAnimation")
def test_simulate(mock_FuncAnimation, mock_axes):
    number_of_frames, frame_delay = 40, 55
    axes_min, axes_max = -600, 1600
    boids = ([0], [0], [0], [0])
    simulate(axes_min, axes_max, number_of_frames, frame_delay, boids, False)
    mock_axes.assert_called_with(
        xlim=(
            axes_min, axes_max), ylim=(
            axes_min, axes_max))
    args = mock_FuncAnimation.call_args
    assert_equal(args[1]['frames'], number_of_frames)
    assert_equal(args[1]['interval'], frame_delay)
