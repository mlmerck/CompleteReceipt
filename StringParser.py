#"ABBEY\nROAD NW8\nCITY OF WESTMINSTER\n"
receipt = recipt= "Barnes & Noble Booksellers #2937\n12193 Fair Lakes Promenade Drive\nairfax, VA 22033\n703-278-0300\nSTR:2937 REG: 006 TRN: 2944 CSHR:Lindsey B\nCode Name Verity\n9781423152830\n(1 9.99)\n9780147508430\n(1 9.99)\n9780062310644\n(1 10.99)\nT1\n9.99\nOut of the Easy\n9.99\nRed Queen Red Queen Series #1)\nT1.\n10.99\nSubtotal\nSales Tax T1 (6.000%)\nTOTAL\nELECTRONIC GIFT CARD\n30.97\n1.86\n32.83\n20.00\nCard#: XXXXXXXXXXX8686\nAuth: 000000\nEntry Method: Swiped\nCard Balance 0.00\nELECTRONIC GIFT CARD\n12.83\nCardH: XXXxXX\nAuth: 0\nEntry Metis Swiped\nCard Balnce:?. 17\n65\nA MEMBER WOUL HAVE SAVED\n3.1\nConmect with us on Socil\na fax\nTwitter- @BJFa 1.fax\n101.44A\n07/23/2017 03:46P\nCUSTOMER COPM"
lineStrings = receipt.split("\n")

# #Store Name
# StoreName = lineStrings[0]
#
# #Store Address
# address = ""
# variable = False
# for lines in range(1, 3):
#    for place in range (1,(len(lineStrings[lines]))-2):
#        if not lineStrings[lines][place].isdigit() and not lineStrings[lines][place]=="."):
#            break
#
#    if variable == True:
#        break
#    else:
#        address = address + lineStrings[lines] + ", "

# def traceItemName(priceIndex)
#     for lines in range(priceIndex,4,-1)
# #item Prices
# prices = []
# items = []
# for lines in range(4, len(lineStrings)):
#    tempBool = False
#    for place in range (0,(len(lineStrings[lines]))):
#        if not lineStrings[lines][place].isdigit() and not lineStrings[lines][place]==".":
#            tempBool = True
#            break
#    if tempBool == True:
#        priceIndex = lines
#        prices.append(lineStrings[lines])
# print(prices)

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
        if lineStrings[lines].find("total")!=-1 or lineStrings[lines].find("Total")!=-1 or lineStrings[lines].find("TOTAL")!=-1:
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
print(prices)
print(items)


    #    count = 0
    #    if stateDigits==2 and lineStrings[lines][place].isdigit():
    #        count = count + 1
    #    else:
    #        count = 0
    #     if count == 5:
    #         isEnd = True
    # if isEnd == True:
    #     break
    # else:
    #     address = address + lineStrings[lines]