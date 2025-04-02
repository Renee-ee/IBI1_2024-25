label_uk = ['England', 'Wales', 'Northern Ireland', 'Scotland'] #put country name into a list label_uk
uk_countries = [57.11, 3.13, 1.91, 5.45] #put data of uk countries into a new list, make sure they are in the same order as label_uk
label_zj = ['Zhejiang', 'Fujian', 'Jiangxi', 'Anhui', 'Jiangsu'] #same as above
zj_provience=[65.77, 41.88, 45.28, 61.27, 85.15] #same as above

#print the data list
print(uk_countries)
print(zj_provience)

#draw the plots
import matplotlib.pyplot as plt
import numpy as np
# Create one figure with two subplots
fig, (plt1, plt2) = plt.subplots(1, 2, figsize=(12, 6))
# Generate colors from light blue to dark blue for the pie chart, making the chart more beautiful
colors1 = plt.cm.Blues(np.linspace(0.4, 1, len(label_uk)))
colors2 = plt.cm.Blues(np.linspace(0.4, 1, len(label_zj)))
#set two subplots
plt1.pie(uk_countries, labels=label_uk, colors=colors1, autopct='%1.2f%%', startangle=90, shadow=True) 
plt1.axis('equal') #make the pie chart into a circle
plt1.set_title("The population in 2022 of component countries in UK")
plt2.pie(zj_provience, labels=label_zj, colors=colors2, autopct='%1.2f%%', startangle=90, shadow=True)
plt2.axis('equal')
plt2.set_title("The population in 2022 of Zhejiang-neighbouring provinces in China")
#put two subplot together
plt.tight_layout()  
plt.show()