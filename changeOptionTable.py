import csv

inFile = open("callNXPI.csv", "r+")
read = csv.reader(inFile)
write = csv.writer(inFile)

# skip header row
next(read)

strikePrice = 127.5

listOfLists = [r for r in read]

for list in listOfLists:
    list.insert(0, strikePrice)

inFile.close()

# calculate profit

maxMultiple = 0
curStrikePrice = 0
for list in listOfLists:
    strikePrice = float(list[4])
    profitPerOption = list[0] - strikePrice

    # option price = ask price
    optionAskPrice = float(list[len(list) - 1])

    # division by 0
    if(optionAskPrice == 0):
        continue

    profitAfterOptionPrice = profitPerOption - optionAskPrice
    returnMultiple = profitAfterOptionPrice/optionAskPrice
    list.append(profitAfterOptionPrice)
    list.append(returnMultiple)

    if(returnMultiple > maxMultiple):
        maxMultiple = returnMultiple
        curStrikePrice=strikePrice

print(maxMultiple)
print(curStrikePrice)
print(listOfLists[0])

# import csv file

# do calculation

# give me top 3 return options

# plot the graph
