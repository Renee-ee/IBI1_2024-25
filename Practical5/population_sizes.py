label_uk = ['England', 'Wales', 'Northern Ireland', 'Scotland']
uk_countries = [57.11, 3.13, 1.91, 5.45]
colors1 = ['#87CEFA', '#6495ED', '#1E90FF', '#4169E1']
label_zj = ['Zhejiang', 'Fujian', 'Jiangxi', 'Anhui', 'Jiangsu']
colors2 = ['#87CEFA', '#6495ED', '#1E90FF', '#4169E1', '#191970']
zj_provience=[65.77, 41.88, 45.28, 61.27, 85.15]

print(uk_countries)
print(zj_provience)

import matplotlib.pyplot as plt1
import numpy as np

plt1.pie(uk_countries, labels=label_uk, colors=colors1, autopct='%1.2f%%', startangle=90, shadow=True)
plt1.axis('equal')
plt1.title(" The population in 2022 of component countries in UK")
plt1.show()

import matplotlib.pyplot as plt2
plt2.pie(zj_provience, labels=label_zj, colors=colors2, autopct='%1.2f%%', startangle=90, shadow=True)
plt2.axis('equal')
plt2.title(" The population in 2022 of the provinces in China which border Zhejiang province")
plt2.show()