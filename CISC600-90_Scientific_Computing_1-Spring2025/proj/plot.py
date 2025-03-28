import matplotlib.pyplot as plt
import numpy as np
from collections.abc import Callable


def graph(
    fn: Callable[[float], float],
    xl: float = 0.01,
    xu: float = 10.0,
    label_x: str = "x-axis",
    label_y: str = "y-axis",
    title: str = "title",
    save_fig: bool = False,
    fig: str = "plot.png",
    show: bool = False,
):
    xp = (xu - xl) / 1000.0
    xpts = np.arange(xl, xu, xp)
    ypts = [fn(x) for x in xpts]

    plt.plot(xpts, ypts)
    plt.xlabel(label_x)
    plt.ylabel(label_y)
    plt.title(title)
    plt.grid(True)

    if save_fig:
        plt.savefig(fig)

    if show:
        plt.show()
