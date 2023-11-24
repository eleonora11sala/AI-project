'''
df_features
Amplitude features
- ASP: amplitude systolic peak
- ADP: amplitude onset peak
- ADN: amplitude dycrotic notch
- RP: ADP/ASP --> augmentation index
- D1: ASP-ADN
- D2: ADP-ADN
- RD: D1/D2
- AMSP: amplitude max slope point (massimo derivata prima)
- RN: ADN/ASP

Time-related feature
- TP: time interval from DP to SP
- T1: time interval from DN to SP
- T2: time interval from DP to DN
- pi2pi_pr: time interval from SPi-1 to SPi
- pi2pi_po time interval from SPi to SPi+1
'''

import numpy as np

def extract_features(df_features, filtered_ppg, fs):

    ##Amplitude features
    peak_pos = df_features['peak_pos']
    mask_onset = df_features['onset'].notnull()
    mask_notch = df_features['diastolic_notch'].notnull()

    df_features['asp'] = filtered_ppg[peak_pos]
    df_features.loc[mask_onset, 'adp'] = filtered_ppg[df_features.loc[mask_onset, 'onset'].astype(int)]
    df_features.loc[mask_notch, 'adn'] = filtered_ppg[df_features.loc[mask_notch, 'diastolic_notch'].astype(int)]

    df_features['rp'] = df_features['adp'] / df_features['asp']
    df_features['d1'] = df_features['asp'] - df_features['adn']
    df_features['d2'] = df_features['adp'] - df_features['adn']
    df_features['rd'] = df_features['d1'] / df_features['d2']
    # AMSP TODO
    df_features['rn'] = df_features['adn'] / df_features['asp']

    ##Time-related features
    df_features['T1'] = df_features['diastolic_notch']/128 - df_features['peak_pos']/128
    df_features['T2'] = df_features['diastolic_notch']/128 - df_features['onset']/128


    # defining pi2pi_pr: time interval from SPi-1 to SPi
    pi2pi_pr = []
    # Add a first 0 value to align the dimension of the array
    pi2pi_pr.append(0)
    for i in range(1, len(df_features)):
        val = df_features.loc[i]['peak_pos'] / fs - df_features.loc[i - 1]['peak_pos'] / fs
        pi2pi_pr.append(val)

    pi2pi_pr = np.array(pi2pi_pr)
    df_features['pi2pi_pr'] = pi2pi_pr


    # pi2pi_po time interval from SPi to SPi+1
    pi2pi_po = []
    for i in range(len(df_features) - 1):
        val = df_features.loc[i + 1]['peak_pos'] / fs - df_features.loc[i]['peak_pos']/ fs
        pi2pi_po.append(val)

    # Add a last None value to align the dimension of the array
    pi2pi_po.append(None)
    pi2pi_po = np.array(pi2pi_po)
    df_features['pi2pi_po'] = pi2pi_po

    return df_features
