import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

os.chdir("C:/Users/Administrator/OneDrive - International Campus, Zhejiang University/桌面/IBI1_2024-25/Practical10")
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")

column3 = dalys_data.iloc[0:10,2] # the 10th year with DALYs data recorded in Afghanistan is 1999
print(column3)


my_raws = []
year = dalys_data.iloc[:,2].tolist()
# type(dalys_data.iloc[:,2])
# dalys_data.iloc[:,2].shape
# dalys_data.iloc[:,2].size

# making the Boolean to show DALYs for all countries in 1990
for y in year:
    # print (type(y)) check the type of y
    if y == 1990: # since the type of y is integer
        my_raws.append(True)
    else:
        my_raws.append(False)
print(dalys_data.loc[my_raws,"DALYs"]) # every row where Year is 1990

# made an object called uk/france to store only the data from the United Kingdom/France
uk = dalys_data.loc[dalys_data.Entity=="United Kingdom", ["DALYs", "Year"]]
france = dalys_data.loc[dalys_data.Entity=="France", ["DALYs", "Year"]]
# Calculate mean DALYs
uk_mean = uk['DALYs'].mean()
france_mean = france['DALYs'].mean()
# Compare means
if uk_mean > france_mean:
    print("UK has higher mean DALYs than France")
elif uk_mean < france_mean:
    print("France has higher mean DALYs than UK") #according to the output, mean DALYs in the UK was greater than France.

# plot showing the DALYS over time in the UK
plt.plot(uk.Year, uk.DALYs, 'b+')
plt.xticks(uk.Year,rotation=-90)  # making the plot nicer (note it is referring to the above subset of data summarising the whole world)
#  Why? What does it do? Change some of the numbers and see what happens if you are unsure.
plt.show()