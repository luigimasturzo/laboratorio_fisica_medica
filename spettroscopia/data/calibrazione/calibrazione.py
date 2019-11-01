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

#x=np.array([60,511,662,1174,1274,1332])   #americio,sodio, cesio, cobalto, sodio, cobalto
x=np.array([54.86,662,1174,1332])
y=np.array([55.19,933.62,1651.43,1874.03])
sigma_y=np.array([10.62,29.46,43.09,41.98])

def linear(x, m, a):
    return m*x+a

popt, pcov = curve_fit(linear, x, y,sigma=sigma_y, p0=[1.,0.])
print(' i parametri trovati sono ( m , a )',popt)
print(' le relative incertezze sono di ',np.sqrt(pcov.diagonal()))
_x = np.linspace(0, 1500, 1500)
_y = linear(_x, *popt)
plt.figure('calibration fit')
plt.plot(_x, _y, label ='fit', alpha=0.8)
plt.errorbar(x,y,yerr=sigma_y, label='data',fmt='.')
plt.xlabel('Energy ( KeV )')
plt.ylabel('channel')
plt.grid()
plt.legend()





chi2 = sum(((y - linear(x, *popt)) / (sigma_y)**2.)
nu = 2
sigma_chi2 = np.sqrt(2 * nu)
print('chi2, dof, incetezza chi2',chi2, nu, sigma_chi2)
print('chi2_red, dof, incetezza chi2_red',chi2/nu, nu, sigma_chi2/nu)

plt.show()