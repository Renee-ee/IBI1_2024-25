#import neccessary libraries
import numpy as np
import matplotlib.pyplot as plt

P = 10000 #population
I = 1 #infected
S = P - I #susceptible
R = 0 #recovered
beta = 0.3 #infection probability
gamma = 0.05 # recovery probability

time = list(range(0, 1001)) # or: time = list(range(1001))
import array
arr_I = array.array('i', [I])  # 'i' specifies integer type
arr_S = array.array('i', [S])
arr_R = array.array('i', [R])

for n in range (1,1001):
    #pick susceptible individuals in susceptible people at random (in probability of beta) to become infected
    I_add = 0
    for i in range (0,S):
        a=np.random.choice (range(2),1,p=[1-beta, beta]) # choose number from range(2) (i.e. 0 or 1) once, with a probability of (1-beta) of choosing 0 and a probability of beta of choosing 1
        if a == 1:
            I_add += 1
    #pick infected individuals in infected people at random (in probability of gamma) to become recovered
    I_minus = 0
    for i in range (0,I):
        b=np.random.choice (range(2),1,p=[1-gamma, gamma])
        if b == 1:
            I_minus += 1
            R += 1
    I = I + I_add - I_minus
    S = P-R-I
    # Add elements for plot
    arr_S.append(S) 
    arr_I.append(I)
    arr_R.append(R)

#plot the result
plt.plot(time, arr_S, label="Susceptible", color="blue") #Susceptible in blue
plt.plot(time, arr_I, label="Infected", color="orange") #Infected in orange
plt.plot(time, arr_R, label="Recovered", color="green") #Recovered in green
plt.xlabel("time")
plt.ylabel("number of people")
plt.title("SIR model")
plt.legend() #add legend
plt.show()

#save the plot as a file
plt.figure(figsize =(6,4),dpi=150) # set your plots as a file with this dimensions and resolution
plt.savefig("<SIR>", type="png")
# !!!Note that Python is not necessarily saving images in the same directory that your python scripts are in.
# !!!You can get around it by specifying the full le path as <filename>