label_uk = ['England', 'Wales', 'Northern Ireland', 'Scotland'] #put country name into a list label_uk
uk_countries = [57.11, 3.13, 1.91, 5.45] #put data of uk countries into a new list, make sure they are in the same order as label_uk
colors1 = ['#87CEFA', '#6495ED', '#1E90FF', '#4169E1'] #make the colors we want to use into a list color1
label_zj = ['Zhejiang', 'Fujian', 'Jiangxi', 'Anhui', 'Jiangsu'] #same as above
colors2 = ['#87CEFA', '#6495ED', '#1E90FF', '#4169E1', '#191970'] #same as above
zj_provience=[65.77, 41.88, 45.28, 61.27, 85.15] #same as above

#print the data list
print(uk_countries)
print(zj_provience)

#draw the plots
import matplotlib.pyplot as plt
# Create one figure with two subplots
fig, (plt1, plt2) = plt.subplots(1, 2, figsize=(12, 6))
#set two subplots
plt1.pie(uk_countries, labels=label_uk, colors=colors1, autopct='%1.2f%%', startangle=90, shadow=True) 
plt1.axis('equal') #make the pie chart into a circle
plt1.set_title(" The population in 2022 of component countries in UK")
plt2.pie(zj_provience, labels=label_zj, colors=colors2, autopct='%1.2f%%', startangle=90, shadow=True)
plt2.axis('equal')
plt2.set_title(" The population in 2022 of the provinces in China which border Zhejiang province")
#put two subplot together
plt.tight_layout()  
plt.show()