import numpy as np

fs = 44100       # sampling rate, Hz, must be integer
duration = 10     # in seconds, may be float

def generateSample(_freqList):
    freqListLen = len(_freqList)
    samplesList = []
    for i in range(freqListLen):
        freq = _freqList[i]
        sample = (np.sin(2*np.pi*np.arange(fs*duration)*freq/fs)).astype(np.float32)
        samplesList.append(sample)

    _audioOutput = sum(samplesList)
    return(_audioOutput)
