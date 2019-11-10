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

_description = 'analize rx '

def andamento(file_path):

    data=np.loadtxt(file_path,unpack=True)


    def expo(x, a, mu):
      return a*np.exp(-mu*x)

    popt, pcov = curve_fit(expo, data[0], data[1],sigma=data[2], p0=[91630., 0.21])
    print(' i parametri stimati sono (a, mu)',popt)
    print(' le relative incertezze sono di ',np.sqrt(pcov.diagonal()))

    _x = np.linspace(np.min(data[0]), np.max(data[0]), 50)
    _y = expo(_x, *popt)
    #_z = expo(_x, popt[0],0.0216)
    plt.figure('fit')
    plt.errorbar(data[0], data[1], yerr=data[2], fmt='.', label='data')
    plt.plot(_x, _y, label='fit')
    #plt.plot(_x,_z,label='best fit')
    plt.xlabel('Spessori [mm]')
    plt.ylabel('Dose uGy')
    plt.title('Andamento Dose in aria in funzione dello spessore')
    plt.legend()
    plt.grid()
    chi2=sum(((data[1]-expo(data[0], *popt))/data[2])**2)
    print('pppp', data[1]-expo(data[0], *popt))
    print('chi2 = {}'.format(chi2))
    print('chi2_norm = ', chi2/3)



if __name__ == '__main__':
    parser=argparse.ArgumentParser(description =_description)
    parser.add_argument('infile', help= 'nome del file Dose')
    args = parser.parse_args()
    andamento(args.infile)






    plt.show()