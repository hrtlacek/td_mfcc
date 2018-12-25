#!/usr/bin/env python
#title           : mfccLibNb.py
#description     : mffc helper functions for the iPython Notebook
#author          : Patrik Lechner <ptk.lechner@gmail.com>
#date            : Dec 2018
#version         : 0.1
#usage           :
#notes           :
#python_version  : 3.6.3
#=======================================================================

import numpy as np
import math
import librosa
from mfccCommon import *

def stft(X, frameSize=4096, windowFunction='hann', overlap=0, absVal=True):
    Y = librosa.stft(X, n_fft=frameSize, hop_length=frameSize -
                     overlap, window=windowFunction)
    if abs:
        return np.abs(Y)
    else:
        return Y
