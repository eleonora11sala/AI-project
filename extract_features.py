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
'''

def extract_features(df_features, filtered_ppg):
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

    return df_features
