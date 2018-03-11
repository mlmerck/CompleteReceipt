import io
import os

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types


"""Detects text in the file."""
client = vision.ImageAnnotatorClient()
path = r"receipt1.jpg"



# def final(filename):
#     global path
#     path = filename
#     pass


with io.open(path, 'rb') as image_file:
   content = image_file.read()

image = types.Image(content=content)

response = client.text_detection(image=image)
texts = response.text_annotations

lineString = []
print(texts)
for text in texts:
    lineString.append(text.description)
temp = lineString[0]
lineStrings = temp.split("\n")



def findStoreName(lineStrings):#code to find the store names
   if "thank" in lineStrings[0] or "Thank" in lineStrings[0]:
    return lineStrings[1]
   else:
    return lineStrings[0]


def findAddress(lineStrings): #code to find the address of the store
   variable = False
   startPoint=1
   lines=0
   if storeName==lineStrings[1]:
       startPoint=2
   for lines in range(startPoint, 5):
       for place in range(1, (len(lineStrings[lines])) - 2):
           if (lineStrings[lines][place - 1] == ' ' and not lineStrings[lines][place].isdigit() and not lineStrings[lines][place + 1].isdigit() and lineStrings[lines][place + 2] == ' '):
               variable = True
               break

       if variable == True:
           break
   if lines==1:
       return lineStrings[startPoint]
   else:
       return lineStrings[lines-1]+" "+lineStrings[lines]

def findTotal(lineStrings):
   total = 0
   testTotal = 0
   for lines in range(3, len(lineStrings)):
       for place in range(1, (len(lineStrings[lines])) - 2):
           if lineStrings[lines][place] == '.' and lineStrings[lines][place + 1].isdigit() and lineStrings[lines][place + 2].isdigit():
               if place + 3 == len(lineStrings[lines]) or lineStrings[lines][place + 3] == " ":
                   if place != 0:
                       temp = place - 1
                   while lineStrings[lines][temp].isdigit() and temp != 0 and lineStrings[lines][temp-1]!='$':
                       temp -= 1
                   #if lineStrings[lines][temp]=='$':
                      # testTotal=float(lineStrings[lines+1][temp:place + 3])
                 #  else:
                   testTotal = float(lineStrings[lines][temp:place + 3])
                   if testTotal > total:
                       total = testTotal
   return total
prices = []
items = []

def findNames(lines):
    for lines in range(lines,3,-1):
        numberCount = 0
        for place in range(0, (len(lineStrings[lines]))):
            if lineStrings[lines][place].isdigit():
                numberCount += 1
        if numberCount<2 and len(lineStrings[lines])>3:
            items.append(lineStrings[lines])
            break


def findItems():
    for lines in range(3, len(lineStrings)):
        if lineStrings[lines].find("total")!=-1 or lineStrings[lines].find("Total")!=-1 or lineStrings[lines].find("TOTAL")!=-1 or lineStrings[lines].find("Amount")!=-1:
            break
        for place in range(1, (len(lineStrings[lines])) - 2):
            if lineStrings[lines][place] == '.' and lineStrings[lines][place + 1].isdigit() and lineStrings[lines][place + 2].isdigit():
                if place + 3 == len(lineStrings[lines]) or lineStrings[lines][place + 3] == " ":
                    if place != 0:
                        temp = place - 1
                    while lineStrings[lines][temp].isdigit() and temp != 0:
                        temp -= 1
                    testTotal = float(lineStrings[lines][temp:place + 3])
                    prices.append(testTotal)
                    findNames(lines)
findItems()

#where the important stuff is happening woo
storeName=findStoreName(lineStrings)#find the storeName
address= findAddress(lineStrings)#find the address
totalPrice= findTotal(lineStrings)


#MAIN
print("The store is:")
print(storeName)
print("")
print("The address is:")
print(address)
print("")

print("Item 1")
print(items[0])
print(prices[0])
print("")
print("Item 2")
print(items[1])
print(prices[1])
print("")
print("Item 3")
print(items[2])
print(prices[2])
print("")
print("The total price is:")
print(totalPrice)








# for text in texts:
#    print('\n"{}"'.format(text.description))

# vertices = (['({},{})'.format(vertex.x, vertex.y)
#            for vertex in text.bounding_poly.vertices])

# print('bounds: {}'.format(','.join(vertices)))


taxfreeprice = 0
for i in prices:
    taxfreeprice += i
percentageprices = []
for i in prices:
    percentageprices.append(i/taxfreeprice)

