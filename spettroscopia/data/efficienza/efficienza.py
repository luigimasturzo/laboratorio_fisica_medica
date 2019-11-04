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

#scelgo il cesio

'''N= 32753.13623174301        #d=10cm ; t=884
s_N= 286.08700458786524
S= 52803*884.819980
A= 0.007
s_N=0.00001
br=0.85
omega=np.pi*(0.5/10)**2
A=omega/(4*np.pi)'''

#ordine:   americio, sodio, cesio, cobalto, sodio, cobalto. 

conteggi=np.array([10510,0,32753.13,25609.05,0,16587.58])
incertezza_conteggi=np.array([131.3,0,286.08,607.82,0,530.93])
attivita=np.array([72277,1478,52803,10719,1478,10719])
tempo=np.array([571.4,5000,884.81,4005.979910,5000,4005.979910])       #corregi sodio
accettanza=np.array([0.007,0.007,0.007,0.007,0.007,0.007])
branching_r=np.array([0.24,1.78,0.85,0.9986,0.9994,0.9986])
energia=np.array([58.4,511,662,1174,1274,1332])

eff=[]

m=len(conteggi)
for i in range(0,m):
    efficienza=conteggi[i]/(attivita[i]*tempo[i]*accettanza[i]*branching_r[i])
    eff.append(efficienza)

eff=np.asarray(eff)

plt.plot(energia,eff)
plt.plot(energia,eff,'.')
plt.show()




'''efficienza=N/(S*A*br)
print(efficienza)'''