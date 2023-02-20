import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
from matplotlib import patches


def plot_signal(
    y: np.ndarray, x_label: str, y_label: str, x_ticks: np.ndarray = np.zeros(1)
) -> None:
    """
    plot_signal _summary_

    Parameters
    ----------
    y : np.ndarray
        y-value array
    x_label : str
        Label of the x-axis
    y_label : str
        Label of the y-axis
    x_ticks : np.ndarray, optional
        Predetermined x-ticks, by default np.zeros(1)
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


def z_plane_plot(
    zeros: np.ndarray,
    poles: np.ndarray,
    save: bool = False,
    sname: str = "z_plane.pdf",
    show: bool = True,
) -> None:
    """
    z_plane_plot is able to plot single and multiple zeros and poles in the z-plane.

    Parameters
    ----------
    zeros : np.ndarray
        array of complex zeros
    poles : np.ndarray
        array of complex poles
    save : bool, optional
        option to save figure, by default False
    sname : str, optional
        define save file name, by default "z_plane.pdf"
    show : bool, optional
        show the plot, by default False

    Returns
    -------
    _type_
        _description_
    """
    offset = 0.05

    def count_values(arr: np.ndarray) -> dict:
        value_counts = {}
        for val in arr:
            if val in value_counts:
                value_counts[val] += 1
            else:
                value_counts[val] = 1
        return value_counts

    value_counts_zeros = count_values(zeros)
    value_counts_poles = count_values(poles)

    mpl.rcParams.update(
        {
            "font.family": "serif",
        }
    )

    ax = plt.subplot(1, 1, 1)
    unit_circle = patches.Circle(
        (0, 0), radius=1, fill=False, color="black", ls="solid", alpha=0.2
    )
    ax.add_patch(unit_circle)
    plt.axvline(0, color="0.8")
    plt.axhline(0, color="0.8")

    poles_plot = plt.plot(poles.real, poles.imag, "x", markersize=9, alpha=1)
    plt.plot(
        zeros.real,
        zeros.imag,
        "o",
        markersize=9,
        color="none",
        alpha=1,
        markeredgecolor=poles_plot[0].get_color(),
    )

    for idx, val in enumerate(value_counts_zeros.values()):
        if val > 1:
            plt.text(
                zeros.real[idx] + offset,
                zeros.imag[idx] + offset,
                f"{val}",
                fontsize=13,
                font="serif",
            )
    for idx, val in enumerate(value_counts_poles.values()):
        if val > 1:
            plt.text(
                poles.real[idx] + offset,
                poles.imag[idx] + offset,
                f"{val}",
                fontsize=13,
                font="serif",
            )

    plt.axis("scaled")
    plt.xlabel("$\Re(z)$")
    plt.ylabel("$\Im(z)$")
    plt.grid(which="both", linestyle="--")
    plt.axis([-1.2, 1.2, -1.2, 1.2])
    plt.tight_layout()
    if save:
        plt.savefig(sname)
    if show is True:
        plt.show()
