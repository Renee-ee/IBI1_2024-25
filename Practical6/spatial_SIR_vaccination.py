#import neccessary libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

beta = 0.3 #infection probability
gamma = 0.05 # recovery probability
alpha = 0.2 #vaccinated probability

# make array of all susceptible population
population = np. zeros( (100, 100) )

# choose one random point in our 100 100 array for where the outbreak happens
outbreak = np.random. choice(range(100) ,2)
population [outbreak[0], outbreak[1]] = 1 

# randomly get the vaccinated people
vaccination= int(alpha *100*100)
c=0
while c<=vaccination:
    v = np.random. choice(range(100) ,2)
    if population [v[0], v[1]] == 0:
        population [v[0], v[1]] = 3
        c += 1

# color the heat map
# 0 = purple (susceptible), 1 = teal (infected), 2 = yellow (recovered), 3 = light green (vaccinated)
cmap = ListedColormap([
    'purple',    # 0
    'teal',      # 1
    'yellow',    # 2
    'lightgreen' # 3
])
plt.figure (figsize =(6,4),dpi=150)
plt.imshow(population, cmap=cmap, interpolation='nearest')
plt.show()


# show model at times 0, 10, 50, and 100
for t in range (1,101):
    # infect the neighbours
    infected = np.where(population == 1) # find the infected points
    for i in range(len(infected[0])):
        infected_x = infected[0][i]
        infected_y = infected[1][i]
        # Check all 8 neighboring cells
        for x in range(infected_x -1, infected_x +2):
            for y in range(infected_y -1, infected_y +2):
                if 0 <= x < 100 and 0 <= y < 100 and population [x,y] == 0:
                    # randomly infect
                    a=np.random.choice ([0,1],p=[1-beta, beta])
                    if a == 1:
                        population [x,y] = 1
    # allow infected individuals to recover
    new_infected = np.where(population == 1)
    for i in range(len(new_infected[0])):
        infected_x = new_infected[0][i]
        infected_y = new_infected[1][i]
        # randomly recover
        b=np.random.choice ([0,1],p=[1-gamma, gamma])
        if b == 1:
            population [infected_x,infected_y] = 2
    if t==10 or t==50 or t==100:
        plt.figure (figsize =(6,4),dpi=150)
        plt.imshow(population, cmap=cmap, interpolation='nearest')
        plt.show()