import matplotlib.pyplot as plt
import numpy as np


def plot_signal(
    y: np.ndarray, x_label: str, y_label: str, x_ticks: np.ndarray = np.zeros(1)
) -> None:
    """
    Plots a stem plot of the input signal

    Parameters
    ----------
    y : np.ndarray
        the y- value array
    x_label : str
        label of the x-axis
    y_label : str
        label of the y-axis
    x_ticks : np.ndarray
        optional parameter for predetermined x-ticks
    """
    if len(x_ticks) == 1:
        x_ticks = np.arange(len(y))
    plt.figure(figsize=(6, 2))
    plt.stem(x_ticks, y, basefmt="k")
    plt.grid()
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()


def plot_sin_cos():
    """Plot sine and cosine in the interval of [0,2pi]"""
    x = np.arange(0, 2 * np.pi, 0.1)
    plt.plot(x, np.sin(x), label="sin(x)")
    plt.plot(x, np.cos(x), label="cos(x)")
    plt.xticks(
        ticks=np.arange(0, 2 * np.pi + 0.1, np.pi / 2),
        labels=["0", "$\pi/2$", "$\pi$", "$3\pi/4$", "$2\pi$"],
    )
    plt.grid()
    plt.legend()
    plt.show()
