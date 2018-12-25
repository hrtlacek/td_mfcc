#!/usr/bin/env python
#title           : mfccCommon.py
#description     : mffc helper functions
#author          : Patrik Lechner <ptk.lechner@gmail.com>
#date            : Dec 2018
#version         : 0.1
#usage           :
#notes           :
#python_version  : 3.6.3
#=======================================================================


import numpy as np
import math

def freqToBin(freqs, sr, frameSize):
    "given the frequencies(array), the sample rate and the frame size; calculates Bin numbers."
    nyq = sr / 2.
    if type(freqs) == int or type(freqs) == float:
        aBin = int(round((freqs / nyq) * frameSize / 2.))
        bins = aBin
    else:
        bins = []

        for i in range(len(freqs)):
            aBin = int(round((freqs[i] / nyq) * frameSize / 2.))
            bins.append(aBin)
    return bins


def hzToMel(f):
    """Converts a Frequency in Hz to Mels"""
    import math
    m = 1125.*math.log(1+f/700.)
    return m


def melToHz(m):
    """Converts Mels to a Frequency Hz"""
    import math
    f = 700.*(math.exp(m/1125)-1)
    return f


def makeMelFilterFreqs(numFilters, lowerFreq, uppperFreq, sr, frameSize):
    mL = hzToMel(lowerFreq)
    mH = hzToMel(uppperFreq)
    filters = np.linspace(mL, mH, numFilters+2)
    filters = [melToHz(x) for x in filters]
    fftBinNumbers = freqToBin(filters, sr, frameSize)
    return fftBinNumbers


def makeMelFilters(nFilters=40, sr=44100, frameLength=4096):
    nFilters = nFilters-4
    centerbins = makeMelFilterFreqs(nFilters, 0, sr/2, sr, frameLength)
    centerbins = [0]+centerbins+[frameLength/2. - 1]
    filters = np.zeros([int(frameLength/2), len(centerbins)])
    for i in range(len(centerbins)-3):
        start = int(centerbins[i])
        center = int(centerbins[i+1])
        end = int(centerbins[i+2])
        filters[start:center, i] = np.linspace(0, 1, center-start)
        filters[center:end, i] = np.linspace(1, 0, end-center)
    return filters


def aToDb(linArray, accuracy=10):
    # A = 20*log10(V2/V1)
    dbArray = 20.*np.log10(np.clip(linArray, 10**-accuracy, 10**accuracy))
    return dbArray


def dBToA(X):
    """Given a np.array calculates linear from dB values"""
    P1 = 10.**(X/20.)
    return P1


def powerSpectrum(spec):
    """spectrum to power spectrum (priodigramm). Includes normalization by framelength.
    
    Arguments:
        spec {np.ndarray} -- the input magnitudes spectrum
    
    Returns:
        np.ndarray -- the periodigramm
    """

    NFFT = spec.shape[0]
    return ((1.0 / NFFT) * ((np.abs(spec)) ** 2))
