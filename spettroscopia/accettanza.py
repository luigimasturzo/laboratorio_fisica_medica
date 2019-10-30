import matplotlib.pyplot as plt
import numpy as np
import random
import math
import time
import os
import argparse
import logging                                                     
logging.basicConfig(level=logging.INFO)    

r=0.5           #cm 
d=20
l=[]
m=1
dd=2
phi_list=[]
theta_list=[]

#genero numeri casuali su una sfera uniforme
b=0
a=0

for j in range (m):

    for i in range(1000000):
        phi=random.uniform(0,2*np.pi)
        epsilon2=random.random()
        theta=np.arccos(1-2*epsilon2)
        phi_list.append(phi)
        theta_list.append(theta)

        #logging.info('phi = {} , theta = {}'.format(phi, theta))

        theta_max=np.arctan((2*r)/(dd+d))
        phi_max=np.arctan((2*r)/(dd+d))

        b +=1

        if (theta>(np.pi)/2 - theta_max and theta<(np.pi)/2 + theta_max and phi>(np.pi)/2 - phi_max and phi<(np.pi)/2 + phi_max):
            a +=1

    A = a/b
    logging.info('la tua accettanza è di = {}'.format(A))
    l.append(1/A)


    phi_list=np.asarray(phi_list)
    theta_list=np.asarray(theta_list)

    plt.figure('ciao ciao')
    plt.hist(phi_list, bins=100, range=(0, 7))
    plt.hist(theta_list, bins=100, range=(0, 7))

    plt.figure('2prova')
    plt.hist(theta_list, bins=100, range=(0, 3.5))



l=np.asarray(l)
A_fin=sum(l)/m
#plt.hist(l,20)
plt.show()






