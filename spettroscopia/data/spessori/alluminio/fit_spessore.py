import matplotlib.pyplot as plt
import numpy as np
import random
import math
import time
import os
import argparse
import logging
from scipy.optimize import curve_fit                                                     
logging.basicConfig(level=logging.INFO)    

def andamento(file_path):

    data=np.loadtxt(file_path,unpack=True)

    def expo(x, a, mu):
      return a*np.exp(-mu*x)

    popt, pcov = curve_fit(expo, data[0], data[1],sigma=data[2], p0=[90000., 0.0189])
    print(' i parametri stimati sono (c, a)',popt)
    print(' le relative incertezze sono di ',np.sqrt(pcov.diagonal()))

    _x = np.linspace(np.min(data[0]), np.max(data[0]), 50)
    _y = expo(_x, *popt)
    plt.figure('fit')
    plt.errorbar(data[0], data[1], yerr=data[2], fmt='.', label='data')
    plt.plot(_x, _y, label='fit')
    plt.legend()
    plt.grid()









if __name__ == '__main__':
    andamento('conteggi_spessori.txt')

    plt.show()
