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
    plt.errorbar(data[0], data[1], yerr=data[2], fmt='.', label='data')
    #plt.plot(_x, _y, label='fit')
    #plt.plot(_x,_z,label='best fit')
    plt.xlabel('Distanza [cm]')
    plt.ylabel('Dose uGy')
    plt.title('Andamento Dose in aria in funzione della distanza')
    plt.legend()
    plt.grid()



if __name__ == '__main__':
    parser=argparse.ArgumentParser(description =_description)
    parser.add_argument('infile', help= 'nome del file Dose')
    args = parser.parse_args()
    andamento(args.infile)






    plt.show()
