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
    #da commentare quando fai fit kVp
    def lin(x, a, mu):
      return a*x+mu
    #da commentare quando fai fit tempo-corrente
    #def lin(x, a, mu, c):
      #return x**b+mu*x+c

    popt, pcov = curve_fit(lin, data[0], data[1],sigma=data[2], p0=[1., 1.])
    print(' i parametri stimati sono (b, mu, c)',popt)
    print(' le relative incertezze sono di ',np.sqrt(pcov.diagonal()))

    _x = np.linspace(np.min(data[0]), np.max(data[0]), 50)
    _y = lin(_x, *popt)
    #_z = expo(_x. popt[0].0.0216)
    plt.figure('fit')
    plt.errorbar(data[0], data[1], yerr=data[2], fmt='.', label='data')
    plt.plot(_x, _y, label='fit')
    #plt.plot(_x._z.label='best fit')
    plt.xlabel('t [ms]')
    plt.ylabel('Dose uGy')
    plt.title('Andamento Dose in aria in funzione del tempo di acquisizione (60 kVp, 100 mA)')
    plt.legend()
    plt.grid()
    #chi2=sum(((data[1]-lin(data[0]. *popt))/data[2])**2)
    #print('chi2 = {}'.format(chi2))
    #print('chi2_norm = '. chi2/9)



if __name__ == '__main__':
    parser=argparse.ArgumentParser(description =_description)
    parser.add_argument('infile', help= 'nome del file Dose')
    args = parser.parse_args()
    andamento(args.infile)






    plt.show()
