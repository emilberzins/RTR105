#Coding: utf-8

#1. N vienmērīgi sadalīti gadījuma skaitļi
# N uniformly distributed random numbers

import sys
sys.path.append("/usr/local/anaconda3/lib/python3.6/site-packages")

from numpy import random
N=1000
x = random.uniform(0,5,N)

"""

k= [0,0,0,0,0]
for i in range(N):
     if x[i]< 1:
          k[0] =k[0]+1
     elif x[i] < 2:
          k[1]=k[1]+1
     elif x[i] <3:
          k[2]=k[2]+1
     elif x[i] <4:
          k[3] = k[3]+1
     else:
        k[4] = k[4]+1
"""
y=random.uniform(0,5,N)
N1= 0
from matplotlib import pyplot as plt
plt.grid()
for i in range(N):
    #plt.plot(x[i],y[i],"ko")
    if x[1] > 0 and x[i] < 5:
        if y[i] >0 and y[i] < x[i]:
            plt.plot(x[i],y[i],"go")
            N1 = N1 +1
        else:
            plt.plot(x[i],y[i],"ro")
            

plt.show()

S_zinaamais = 5*5
S_nezinaamais = 1. * S_zinaamais * N1/N
print(S_nezinaamais)

        
           
