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

#le x energie
#y canali

#x=np.array([60,511,662,1174,1274,1332])   #americio,sodio, cesio, cobalto, sodio, cobalto
x=np.array([59.5409,511,662,1174,1274,1332])
y=np.array([55.19,722.83,933.62,1651.43,1805.08,1874.03])
sigma_y=np.array([10.62,28.10,29.46,43.09,40.98,41.98])
usigma=np.array([0.8,0.3,0.3,0.4,0.4,0.3])
umu=np.array([0.8,0.2,0.2,0.3,0.4,0.3])

urisoluzione=2.35*np.sqrt((usigma/y)**2 + (sigma_y*umu/(y**2))**2)
#urisoluzione=np.log(urisoluzione)

def linear(x, m, a):
    return m*x+a

popt, pcov = curve_fit(linear, x, y,sigma=sigma_y, p0=[1.5,-29])
print(' i parametri trovati sono ( m , a )',popt)
print(' le relative incertezze sono di ',np.sqrt(pcov.diagonal()))
_x = np.linspace(0, 1500, 1500)
_y = linear(_x, *popt)
plt.figure('calibration fit')
plt.plot(_x, _y, label ='fit', alpha=0.9)
plt.errorbar(x,y,yerr=sigma_y,label='dati',fmt='.')
plt.xlabel(' Energia ( Chn ) ')
plt.ylabel(' Canali ')
plt.grid()
plt.legend()
chi21=sum(((y-linear(x, *popt))/sigma_y)**2)
print('chi2lin= {}'.format(chi21/4))


#Risoluzione enrgetica = 2.36*sigma/mu
risoluzione=2.35*sigma_y/y
#risoluzione=np.log(risoluzione)
#x=np.log(x)
def rad(y, m, a):
    return m/(y**a)
def rad2(y, m, a):
    return m*y+a

popt, pcov = curve_fit(rad, y, risoluzione,sigma=urisoluzione ,p0=[3.2,0.5])
print(' i parametri trovati sono ( emmm , aaa )',popt)
print(' le relative incertezze sono di ',np.sqrt(pcov.diagonal()))
plt.figure('risoluzione enrgetica')
_x = np.linspace(1, 2000, 2050)
_y = rad(_x, *popt)
#plt.yscale('log')
plt.plot(_x, _y, label ='fit', alpha=0.8)
#plt.plot(x,risoluzione,'.')
#plt.figure('punti')
plt.errorbar(y,risoluzione,yerr=urisoluzione,xerr=umu,label='dati',fmt='.')
plt.xlabel(' Energia ( Chn ) ')
plt.ylabel(' R ')
plt.grid()
plt.legend()
chi2=sum(((risoluzione-rad(y, *popt))/urisoluzione)**2)
print(chi2/4)
print(risoluzione)
print(urisoluzione)






'''chi2 = sum(((y - linear(x, *popt)) / (sigma_y))**2.)
print(chi2)
chi3 = sum(((risoluzione - rad(x, *popt)) / (urisoluzione))**2.)
print(chi3/4)





sigma_chi2 = np.sqrt(2 * nu)
print('chi2, dof, incetezza chi2',chi2, nu, sigma_chi2)
print('chi2_red, dof, incetezza chi2_red',chi2/nu, nu, sigma_chi2/nu)'''

plt.show()
