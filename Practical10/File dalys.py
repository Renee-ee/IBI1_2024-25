# Import necessary libraries
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Change working directory
os.chdir("C:/Users/Administrator/OneDrive - International Campus, Zhejiang University/桌面/IBI1_2024-25/Practical10")
# Load the dataset
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")


# -----------------------
# Showing 3rd column (the year) for the first 10 rows
# -----------------------
column3 = dalys_data.iloc[0:10, 2]
print("First 10 values of the 'Year' column:")
print(column3,'\n')
# COMMENT: The 10th year with DALYs data recorded in Afghanistan is 1999
afghanistan = dalys_data[dalys_data["Entity"] == "Afghanistan"]
print("10th year with DALYs data for Afghanistan:", afghanistan.iloc[9, 2],'\n')


# -----------------------
# Boolean indexing for Year == 1990
# -----------------------
# Creating a Boolean list to select DALYs for Year 1990
my_raws = []
year = dalys_data.iloc[:,2].tolist()
for y in year:
    if y == 1990: # the type of y is integer
        my_raws.append(True)
    else:
        my_raws.append(False)
print("DALYs for all countries in 1990:")
print(dalys_data.loc[my_raws,"DALYs"],'\n') # every row where Year is 1990


# -----------------------
# Compare UK and France mean DALYs
# -----------------------
uk = dalys_data.loc[dalys_data.Entity=="United Kingdom", ["DALYs", "Year"]] # made an object called uk/france to store only the data from the United Kingdom/France
france = dalys_data.loc[dalys_data.Entity=="France", ["DALYs", "Year"]]

uk_mean = uk['DALYs'].mean() # Calculate mean DALYs
france_mean = france['DALYs'].mean()

print('UK mean DALYs: ', uk_mean)
print('France mean DALYs: ', france_mean)

if uk_mean > france_mean: # Compare means
    print("UK has higher mean DALYs than France")
elif uk_mean < france_mean:
    print("France has higher mean DALYs than UK") 
# COMMENT: according to the output, mean DALYs in the UK was greater than France.


# -----------------------
# Plot UK DALYs over time
# -----------------------
plt.plot(uk.Year, uk.DALYs, 'b+')
plt.title("DALYs in the United Kingdom Over Time")
plt.xlabel("Year")
plt.ylabel("DALYs")
plt.xticks(uk.Year,rotation=-90)  # making the plot nicer (note it is referring to the above subset of data summarising the whole world)
plt.show()


# -----------------------
# UK vs France comparison plot
# -----------------------
plt.plot(uk['Year'], uk['DALYs'], 'ro', label='United Kingdom')  # 'ro' = red circles
plt.plot(france['Year'], france['DALYs'], 'b^', label='France')  # 'b^' = blue triangles
plt.title('DALYs Over Time (UK vs. France)')
plt.xlabel('Year')
plt.ylabel('DALYs Rate')
plt.legend()
plt.show()


# -----------------------
# Answer custom question
# Question: How has the relationship between the DALYs in China and the UK changed over time?
#           Are they becoming more similar, less similar?
# Line number for question.txt = 81
# -----------------------
# Filter data for China and UK
china = dalys_data[dalys_data["Entity"] == "China"]
uk = dalys_data[dalys_data["Entity"] == "United Kingdom"]
# Ensure years match in both datasets (intersection only)
common_years = set(china["Year"]).intersection(set(uk["Year"]))
china_common = china[china["Year"].isin(common_years)].sort_values("Year")
uk_common = uk[uk["Year"].isin(common_years)].sort_values("Year")
# Calculate the absolute difference between DALYs in China and the UK
difference = abs(china_common["DALYs"].values - uk_common["DALYs"].values)
# Plot DALYs and the difference for both countries
plt.plot(china_common["Year"], china_common["DALYs"], 'r+', label='China')
plt.plot(uk_common["Year"], uk_common["DALYs"], 'b+', label='United Kingdom')
plt.plot(china_common["Year"], difference, 'mo', label='Absolute Difference (China - UK)')
plt.title("DALYs in China vs UK Over Time")
plt.xlabel("Year")
plt.ylabel("DALYs")
plt.legend()
plt.xticks(china_common["Year"], rotation=-90)
plt.show()