
import numpy as np
def artifacts(speaks, filtered_ppg, annotations):
    adp = []
    for i in range(len(speaks)):
        if (abs(filtered_ppg[speaks[i]]) > 2):
            adp.append(i);
    adp = np.squeeze(adp)

    speaks = np.delete(speaks, adp)
    annotations = np.delete(annotations, adp)

    return speaks, annotations
