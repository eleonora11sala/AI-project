import numpy as np
import scipy.io

def preprocess(signal):
    # Denoising --> second-order Butterworth filter
    signal_temp_unidimensional = np.ravel(signal)
    # Let's run it through a standard butterworth bandpass implementation to remove everything < 0.8 and > 3.5 Hz.
    b, a = scipy.signal.butter(2, [0.5, 8], btype='bandpass', analog=False, output='ba', fs=128)
    filtered_ppg = scipy.signal.filtfilt(b, a, signal_temp_unidimensional)

    # Detrend
    filtered_ppg = scipy.signal.detrend(filtered_ppg, axis=-1, type='linear', bp=0, overwrite_data=True)

    return filtered_ppg