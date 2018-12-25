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
from mfccCommon.py import *

# def freqToBin(freqs, sr, frameSize):
#     "given the frequencies(array), the sample rate and the frame size; calculates Bin numbers."
#     nyq = sr / 2.
#     if type(freqs) == int or type(freqs) == float:
#         aBin = int(round((freqs / nyq) * frameSize / 2.))
#         bins = aBin
#     else:
#         bins = []

#         for i in range(len(freqs)):
#             aBin = int(round((freqs[i] / nyq) * frameSize / 2.))
#             bins.append(aBin)
#     return bins


# def hzToMel(f):
#     """Converts a Frequency in Hz to Mels"""
#     import math
#     m = 1125.*math.log(1+f/700.)
#     return m


# def melToHz(m):
#     """Converts Mels to a Frequency Hz"""
#     import math
#     f = 700.*(math.exp(m/1125)-1)
#     return f


# def makeMelFilterFreqs(numFilters, lowerFreq, uppperFreq, sr, frameSize):
#     mL = hzToMel(lowerFreq)
#     mH = hzToMel(uppperFreq)
#     filters = np.linspace(mL, mH, numFilters+2)
#     filters = [melToHz(x) for x in filters]
#     fftBinNumbers = freqToBin(filters, sr, frameSize)
#     return fftBinNumbers


def stft(X, frameSize=4096, windowFunction='hann', overlap=0, absVal=True):
    Y = librosa.stft(X, n_fft=frameSize, hop_length=frameSize -
                     overlap, window=windowFunction)
    if abs:
        return np.abs(Y)
    else:
        return Y


# def powerSpectrum(spec):
#     """spectrum to power spectrum (priodigramm). Includes normalization by framelength.
    
#     Arguments:
#         spec {np.ndarray} -- the input magnitudes spectrum
    
#     Returns:
#         np.ndarray -- the periodigramm
#     """

#     NFFT = spec.shape[0]
#     return ((1.0 / NFFT) * ((np.abs(spec)) ** 2))


# def aToDb(linArray, accuracy=10):
#     # A = 20*log10(V2/V1)
#     dbArray = 20.*np.log10(np.clip(linArray, 10**-accuracy, 10**accuracy))
#     return dbArray


# def dBToA(X):
#     """Given a np.array calculates linear from dB values"""
#     P1 = 10.**(X/20.)
#     return P1
