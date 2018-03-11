import os
import matplotlib.pyplot as plt
import testdata as expensedata

#takes cost data and finds average costs
costs = expensedata.costs
totalcost = 0
for i in costs:
    totalcost += i
percentagecost = []
for i in costs:
    percentagecost.append(i/totalcost)


# Pie chart
labels = expensedata.costtypes
count = 0
labels1 = []
for i in labels:
    labels1.append(labels[count].title())
    count += 1

sizes = percentagecost
# colors
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']

fig1, ax1 = plt.subplots()
ax1.pie(sizes, colors=colors, labels=labels1, autopct='%1.1f%%', startangle=90)
# draw circle
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
# Equal aspect ratio ensures that pie is drawn as a circle
ax1.axis('equal')
fig1.set_facecolor((230/255,233/255,239/255,1))
plt.tight_layout()

#Saves file ONLY COMMENT LINE 39 OUT THE FIRST TIME YOU RUN THIS CODE!!!!!!!!!
#os.remove("/Users/Matthew/Documents/Receipt-Bag/piechart1.png")
fig1.savefig('piechart1.png', facecolor=fig1.get_facecolor(), edgecolor='none')
