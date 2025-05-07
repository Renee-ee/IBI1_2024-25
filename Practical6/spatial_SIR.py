#import neccessary libraries
import numpy as np
import matplotlib.pyplot as plt

# make array of all susceptible population
population = np. zeros( (100, 100) )
# 0/dark purple for susceptible, 1/lue-green for infected, 2/yellow for recovered

# choose one random point in our 100 100 array for where the outbreak happens
outbreak = np.random. choice(range(100) ,2)
population [outbreak[0], outbreak[1]] = 1

# color the heat map
plt.figure (figsize =(6,4),dpi=150)
plt.imshow (population , cmap='viridis', interpolation='nearest')
plt.show()

beta = 0.3 #infection probability
gamma = 0.05 # recovery probability


# show model at times 0, 10, 50, and 100

for t in range (1,101):
    # infect the neighbours
    infected = np.where(population == 1) # find the infected points
    print (type(infected))
    print (infected)
    for i in range(len(infected[0])):
        infected_x = infected[0][i]
        infected_y = infected[1][i]
        for x in range(infected_x -1, infected_x +2):
            for y in range(infected_y -1, infected_y +2):
                if 0 <= x < 100 and 0 <= y < 100 and population [x,y] == 0:
                    a=np.random.choice ([0,1],p=[1-beta, beta]) # choose number from range(2) (i.e. 0 or 1) once, with a probability of (1-beta) of choosing 0 and a probability of beta of choosing 1
                    if a == 1:
                        population [x,y] = 1
    #allow infected individuals to recover
    new_infected = np.where(population == 1)
    for i in range(len(new_infected[0])):
        infected_x = new_infected[0][i]
        infected_y = new_infected[1][i]
        b=np.random.choice ([0,1],p=[1-gamma, gamma])
        if b == 1:
            population [infected_x,infected_y] = 2
    if t==10 or t==50 or t==100:
        print (0)
        plt.figure (figsize =(6,4),dpi=150)
        plt.imshow (population , cmap='viridis', interpolation='nearest')
        plt.show()