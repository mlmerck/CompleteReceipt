import os
import matplotlib.pyplot as plt
import ReceiptBagBackend as dataaa



#takes cost data and finds average costs
costs = [9.85, 26.32, 30.97]
totalcosts = 67.14
percentagecost = [9.85/67.14, 26.32/67.14, 30.97/67.14]

print(percentagecost)

# Pie chart
labels = dataaa.items
count = 0
labels1 = ["Surfside", "Papa Johns", "Barnes and Noble"]
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

#Saves file
#os.remove('''C:\Users\Jared\PycharmProjects\ReceiptBag\piechart1.png''')
fig1.savefig('piechart4.png', facecolor=fig1.get_facecolor(), edgecolor='none')