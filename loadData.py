import scipy.io
import numpy as np, os

def loadData(ROOT_PATH):
    mat1 = scipy.io.loadmat(ROOT_PATH + '/S001_128.mat')
    mat2 = scipy.io.loadmat(ROOT_PATH + '/S001_128_ann.mat')
    mat3 = scipy.io.loadmat(ROOT_PATH + '/S001_128_spk.mat')

    recording = np.asarray(mat1['ppg'], dtype=np.float64)

    # Get number of ann files contained in the folder
    path_ppgs_128 = []
    path_ppgs_250 = []
    for f in os.listdir(ROOT_PATH):
        g = os.path.join(ROOT_PATH, f)
        if not f.lower().startswith('.') and f.lower().endswith('_128.mat') and os.path.isfile(g):
            path_ppgs_128.append(g)
        elif not f.lower().startswith('.') and f.lower().endswith('_250.mat') and os.path.isfile(g):
            path_ppgs_250.append(g)

    num_files_128 = len(path_ppgs_128)
    num_files_250 = len(path_ppgs_250)

    '''
    print("cases 128: ")
    print(num_files_128)
    print("cases 250: ")
    print(num_files_250)
    print("Tot: ")
    print(num_files_128 + num_files_250)
    '''

    # Create empty list for annotation, peak position and ppg signals of files
    # Annotation: labels which can assume 3 values: N (Normal), V (Ventricular), S(SuperVentricular)
    # speaks: contains peak positions in samples
    # ppg: contains the ppg signal in samples
    annotations_128 = list()
    speaks_128 = list()
    ppgs_128 = list()

    # Load files for each subject using the function "loadmat"
    for i in range(num_files_128):
        print('Loading file: ' + str(i + 1) + '/' + str(num_files_128))
        root = path_ppgs_128[i].split("_")
        ppgMat = scipy.io.loadmat(path_ppgs_128[i])
        ppg = np.asarray(ppgMat['ppg'], dtype=np.float64)
        annotationMat = scipy.io.loadmat(root[0] + '_128_ann.mat')
        annotation = np.asarray(annotationMat['labels'])
        speaksMat = scipy.io.loadmat(root[0] + '_128_spk.mat')
        speaks = np.asarray(speaksMat['speaks'])

        annotations_128.append(annotation)
        speaks_128.append(speaks)
        ppgs_128.append(ppg)

    annotations_250 = list()
    speaks_250 = list()
    ppgs_250 = list()

    # Load files for each subject using the function "loadmat"
    for i in range(num_files_250):
        print('Loading file: ' + str(i + 1) + '/' + str(num_files_250))
        root = path_ppgs_250[i].split("_")
        ppgMat = scipy.io.loadmat(path_ppgs_250[i])
        ppg = np.asarray(ppgMat['ppg'], dtype=np.float64)
        annotationMat = scipy.io.loadmat(root[0] + '_250_ann.mat')
        annotation = np.asarray(annotationMat['labels'])
        speaksMat = scipy.io.loadmat(root[0] + '_250_spk.mat')
        speaks = np.asarray(speaksMat['speaks'])

        annotations_250.append(annotation)
        speaks_250.append(speaks)
        ppgs_250.append(ppg)

    return  ppgs_128, speaks_128, annotations_128, ppgs_250, speaks_250, annotations_250