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
    print(data, type(data), data[0], data[1])

    #data[0]=data[0]-2.054

    def quadratic(x, a, b):
      return a/(b**2 + x**2)

    popt, pcov = curve_fit(quadratic, data[0], data[1],sigma=data[2], p0=[70000., 0.])
    print(' i parametri stimati sono (c, a)',popt)
    print(' le relative incertezze sono di ',np.sqrt(pcov.diagonal()))

    _x = np.linspace(np.min(data[0]), np.max(data[0]), 50)
    _y = quadratic(_x, *popt)
    plt.figure('fit')
    #plt.plot(data[0], data[1],'.', label='data', alpha=1)
    plt.errorbar(data[0], data[1], data[2], fmt='.', label='data')
    plt.plot(_x, _y, label='fit')
    plt.legend()
    plt.grid()









if __name__ == '__main__':
    andamento('distanza_conteggi.txt')

    plt.show()
