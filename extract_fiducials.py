import numpy as np
import pandas as pd

from dotmap import DotMap
from pyPPG import PPG, Fiducials, Biomarkers
import pyPPG.fiducials as FP

def check_speak(speak, signal):
    temp = speak
    prec = speak - 1
    post = speak + 1
    if (signal[temp] < signal[post] and signal[temp] > signal[prec]):
        while (signal[temp] < signal[post]):
            temp = post
            post += 1
    elif (signal[temp] > signal[post] and signal[temp] < signal[prec]):
        while (signal[temp] < signal[prec]):
            temp = prec
            prec -= 1

    return temp


def find_on(peaks,fiducials):
    on=[]
    for p in range(len(peaks)):
        arr=[]
        arr=fiducials['on'].loc[fiducials['sp']>np.squeeze(peaks[p])-5]
        if(isinstance(np.squeeze(arr[0:1]), np.int64)):
            on.append(np.squeeze(arr[0:1]))
        else:
            on.append(None)
    return on


def find_dn(peaks, fiducials):
    dn = []
    for p in range(len(peaks)):
        arr = []
        arr = fiducials['dn'].loc[fiducials['sp'] > np.squeeze(peaks[p]) - 5]
        if (isinstance(np.squeeze(arr[0:1]), np.int64)):
            dn.append(np.squeeze(arr[0:1]))
        else:
            dn.append(None)

    return dn


def extract_fiducials(signal, peaks):
    sig = DotMap()
    sig.filt_sig = signal
    sig.v = signal
    sig.filt_d1 = signal
    sig.filt_d2 = signal
    sig.filt_d3 = signal
    sig.fs = 128
    sig.ppg

    a = PPG(s=sig)
    fpex = FP.FpCollection(s=a)
    fiducials = fpex.get_fiducials(s=a)

    speaks_check = []
    for i in range(len(peaks)):
        speaks_check.append(int(check_speak(peaks[i], signal)[0]))

    on = find_on(speaks_check, fiducials)
    dn = find_dn(speaks_check, fiducials)

    df_fiducials = pd.DataFrame({
        # Execute -1 because matlab start counting from 1
        'peak_pos': speaks_check,
        'onset': on,
        'diastolic_notch': dn
    })

    return df_fiducials