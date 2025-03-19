lan = {'JavaScipt': 62.3, 'HTML': 52.9, 'Python': 51, 'SQL': 51, "TypeScript": 38.5 }
print (lan)

import matplotlib.pyplot as plt
import numpy as np

plt.bar(lan.keys(), lan.values(), color='cyan')
plt.xlabel('Language')
plt.ylabel('User(percentage)')
plt.title('Programming language popularity')
plt.show()