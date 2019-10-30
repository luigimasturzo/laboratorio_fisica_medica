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

#le x sono i canali
#y energie

x=np.array([60,511,662,1174,1274,1332])   #americio, sodio, cesio, cobalto, sodio, cobalto
y=np.array([])
sigma_y=np.array([])

def linear(x, a, m):
    return m*x+a

popt, pcov = curve_fit(linear, x, y,sigma_y p0=[1,0])
print(' i parametri trovati sono ( m, a )',popt)
print(' le relative incertezze sono di ',np.sqrt(pcov.diagonal()))
_x = np.linspace(0, 1500, 1500)
_y = linear(_x, *popt)
plt.figure('calibration fit')
plt.plot(_x, _y)




chi2 = sum(((y - linear(x, *popt)) / sigma_y)**2.)
nu = 4
sigma_chi2 = np.sqrt(2 * nu)
print('chi2, dof, incetezza chi2',chi2, nu, sigma)
print('chi2_red, dof, incetezza chi2_red',chi2/nu, nu, sigma/nu)