import numpy as np


def circ_conv(sign_1: np.ndarray, sign_2: np.ndarray) -> np.ndarray:
    """
    circ_conv computes the circular convolution.

    Parameters
    ----------
    sign_1 : np.ndarray
        Real valued 1D array
    sign_2 : np.ndarray
        Real valued 1D array

    Returns
    -------
    np.ndarray
        Circular convolution
    """
    return np.real(np.fft.ifft(np.fft.fft(sign_1) * np.fft.fft(sign_2)))


def norm_data(data: np.ndarray, low_bound: int = 0, high_bound: int = 1) -> np.ndarray:
    """
    Normalise data to a given boundary. If the data is complex the absolute value ist computed.

    Parameters
    ----------
    data : np.ndarray
        data
    low_bound : int, optional
        lower boundary, by default 0
    high_bound : int, optional
        above boundary, by default 1

    Returns
    -------
    np.ndarray
        absolute and normalized data
    """

    norm_data = []
    diff = high_bound - low_bound
    diff_arr = max(data) - min(data)
    for i in data:
        temp = (((i - min(data)) * diff) / diff_arr) + low_bound
        norm_data.append(temp)
    return np.array(norm_data)
