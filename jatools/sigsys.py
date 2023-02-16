import numpy as np


def circ_conv(sign_1: np.ndarray, sign_2: np.ndarray) -> np.ndarray:
    """Computes the circular convolution.

    Parameter
    ---------
    sign_1 : np.ndarray
        real 1D array
    sign_2 : np.ndarray
        real 1D array

    Returns
    ------
    np.ndarray
        computed circular convolution
    """
    return np.real(np.fft.ifft(np.fft.fft(sign_1) * np.fft.fft(sign_2)))
