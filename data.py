import os
import matplotlib.pyplot as plt

# Pie chart
labels = ['Fast Food', 'Gasoline', 'Utilities', 'Miscellaneous']
sizes = [15, 30, 45, 10]
# colors
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']

fig1, ax1 = plt.subplots()
ax1.pie(sizes, colors=colors, labels=labels, autopct='%1.1f%%', startangle=90)
# draw circle
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
# Equal aspect ratio ensures that pie is drawn as a circle
ax1.axis('equal')
fig1.set_facecolor((230/255,233/255,239/255,1))
plt.tight_layout()

#Saves file
os.remove("/Users/Matthew/Documents/Receipt-Bag/piechart1.png")
fig1.savefig('piechart1.png', facecolor=fig1.get_facecolor(), edgecolor='none')

