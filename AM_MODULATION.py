#!/usr/bin/env python
# coding: utf-8

# # Modulação AM - Projeto 6 - Camada Física da Computação
# 
# Eiki Yamashiro | 4º Semestre Engenharia de Computação | Insper - Instituto de Ensino e Pesquisa

# In[ ]:


import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import winsound
import sounddevice as sd
import pandas as pd
from scipy import signal
from scipy.fftpack import fft, fftshift
import peakutils
import soundfile   as sf
import math


# In[5]:


def calcFFT(signal, fs):
    # https://docs.scipy.org/doc/scipy/reference/tutorial/fftpack.html
    #y  = np.append(signal, np.zeros(len(signal)*fs))
    N  = len(signal)
    T  = 1/fs
    xf = np.linspace(-1.0/(2.0*T), 1.0/(2.0*T), N)
    yf = fft(signal)
    return(xf, fftshift(yf))


# In[6]:


def generateSin(freq, time, fs):
    n = time*fs #numero de pontos
    x = np.linspace(0.0, time, n)  # eixo do tempo
    s = np.sin(freq*x*2*np.pi)
    return (x, s)


# In[7]:


def plotFFT(signal, fs):
    x,y = calcFFT(signal, fs)
    plt.figure()
    plt.plot(x, np.abs(y))
    plt.title('Fourier')
    plt.show()
    return x,y


# In[8]:


def LPF(signal, cutoff_hz, fs):
        from scipy import signal as sg
        #####################
        # Filtro
        #####################
        # https://scipy.github.io/old-wiki/pages/Cookbook/FIRFilter.html
        nyq_rate = fs/2
        width = 5.0/nyq_rate
        ripple_db = 60.0 #dB
        N , beta = sg.kaiserord(ripple_db, width)
        taps = sg.firwin(N, cutoff_hz/nyq_rate, window=('kaiser', beta))
        return( sg.lfilter(taps, 1.0, signal))


# In[9]:


def main():
    str_audio = input("Digite o nome do arquivo (.wav): ")
    
    fs = 44100
    F = 1
    T = 1
    
    p = 14000
    
    sd.default.samplerate = fs
    sd.default.channels = 1
    notNorm = []
    returnList = []
    audio, samplerate = sf.read("audios/{}".format(str_audio))
    yAudio = audio[:,1]
    samplesAudio = len(yAudio)
    t = np.linspace(0, samplesAudio/fs, samplesAudio)
    port = np.cos(2*np.pi*p*t)
    
#======================================================ORIGINAL============================================================
    
    #O Audio já estava entre 1 e -1, então multipliquei por 5 para atingir valores que não pertencem ao conjunto [-1 ; 1].
    for e in yAudio:
        e = e*5
        notNorm.append(e)
    #Plot do audio sem a normalização:
    
    
    plt.plot(t, notNorm, color="orange")
    plt.grid()
    plt.title('Audio Original')
    plt.show()
    
    X1, Y1 = calcFFT(notNorm, 44100)
    plt.plot(X1, np.abs(Y1), color="orange")
    plt.grid()
    plt.title('Frequencia Original')
    plt.show()
    
    sd.play(notNorm)
    sd.wait()
    
    print("-----------------------------------------------------------------------")

#======================================================FILTRO============================================================
    
    maxPoint = max(notNorm)
    
    for e in notNorm: 
        returnList.append(e/maxPoint)
    
    #Plot do audio normalizado:
    plt.plot(t, returnList, color="olive")
    plt.grid()
    plt.title("Audio Normalizado")
    plt.show()
    
    X2, Y2 = calcFFT(returnList, 44100)
    plt.plot(X2, np.abs(Y2), color="olive")
    plt.grid()
    plt.title('Frequencia Normalizada')
    plt.show()
    
    sd.play(returnList)
    sd.wait()
    
    print("-----------------------------------------------------------------------")

#======================================================MODULAÇÃO============================================================

    filtrado = LPF(returnList, 4000, fs)
    
    plt.plot(t, filtrado, color="brown")
    plt.grid()
    plt.title("Audio Filtrado")
    plt.show()
    
    X, Y = calcFFT(filtrado, 44100)
    plt.plot(X, np.abs(Y), color="brown")
    plt.grid()
    plt.title('Frequencia Filtrada')
    plt.show()
    
    sd.play(filtrado)
    sd.wait()
    
    print("-----------------------------------------------------------------------")
    
    mod = 1*filtrado*port
    
    plt.plot(t, mod, color="green")
    plt.grid()
    plt.title("Audio Modulado")
    plt.show()
    
    X3, Y3 = calcFFT(mod, samplerate)
    plt.plot(X3, np.abs(Y3), color="green")
    plt.grid()
    plt.title('Frequencia Modulada')
    plt.show()
    
    sd.play(mod)
    sd.wait()
    
    print("-----------------------------------------------------------------------")
    
#======================================================DEMODULAÇÃO============================================================
    
    demod = port*mod
    
    plt.plot(t, demod)
    plt.grid()
    plt.title("Audio Demodulado")
    plt.show()
    
    X4, Y4 = calcFFT(demod, samplerate)
    plt.plot(X4, np.abs(Y4))
    plt.grid()
    plt.title('Frequencia Demodulada')
    plt.show()
    
    sd.play(demod)
    sd.wait()
    


# In[10]:


main()


# In[ ]:




