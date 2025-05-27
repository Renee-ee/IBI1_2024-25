#import neccessary libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm # color map (for the plot)

P = 10000 #population
I = 1 #infected
beta = 0.3 #infection probability
gamma = 0.05 #recovery probability
alpha = [0,10,20,30,40,50,60,70,80,90,100] #vaccinated probability

time = list(range(0, 1001)) # or: time = list(range(1001))
colors = [[1, 0, 0],[1, 0.5, 0],[1, 0.647, 0],[1, 0.75, 0],[1, 1, 0],[0.6, 1, 0],[0, 1, 0],[0, 0.7, 1],[0, 1, 1],[0, 0, 1],[0.5, 0, 0.5]]

import array
arr_I = array.array('i', [I])  # 'i' specifies integer type

for m in range(0,11):
    V = int(alpha[m]*P/100) #vaccinated
    I = 1 #infected
    R = 0 #recovered
    S = P-I-R-V #susceptible
    for n in range (1,1001):
        #pick susceptible individuals at random to become infected
        I_add = 0
        for i in range (0,S):
            a=np.random.choice ([0,1],p=[1-beta, beta])
            if a == 1:
                I_add += 1
        #pick infected individuals at random to become recovered
        I_minus = 0
        for i in range (0,I):
            b=np.random.choice ([0,1],p=[1-gamma, gamma])
            if b == 1:
                I_minus += 1
                R += 1
        I = I + I_add - I_minus
        S = P-I-R-V
        arr_I.append(I) # Add element
    plt.plot(time, arr_I, label= str(alpha[m])+"%", color= colors[m])
    #plt.plot(time, arr_I, label= str(alpha[m])+"%", color=cm.viridis(30)) # plots the dataset using colour number 30 (a sort of blue) from the viridis colour map.
    arr_I = array.array('i', [1])

plt.xlabel("time")
plt.ylabel("number of people")
plt.title("SIR model with different vaccination rates")
plt.legend() #add legend
plt.show()

#save the plot as a file
plt.figure(figsize =(6,4),dpi=150) # set your plots as a file with this dimensions and resolution
plt.savefig("SIR_vaccination.png")
# !!!Note that Python is not necessarily saving images in the same directory that your python scripts are in.
# !!!You can get around it by specifying the full le path as <filename>