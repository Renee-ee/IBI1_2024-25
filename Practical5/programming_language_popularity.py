#firstly put all the data into a dictionary lan
lan = {'JavaScript': 62.3, 'HTML': 52.9, 'Python': 51, 'SQL': 51, "TypeScript": 38.5 }
print (lan)

#use the matplot to draw a plot
import matplotlib.pyplot as plt
import numpy as np
#setting the bar chart
plt.bar(lan.keys(), lan.values(), color='cyan')
plt.xlabel('Language')
plt.ylabel('User(percentage)')
plt.title('Programming language popularity')
plt.show()

#out put the input language percentage
requested_language = "Python"  # <- this can be changed
if requested_language in lan:
    print(f"\nThe percentage of developers who use {requested_language} is {lan[requested_language]}%.")
else:
    print(f"\n{requested_language} is not in the data.")