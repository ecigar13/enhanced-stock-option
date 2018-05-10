import csv
from operator import itemgetter

# import csv file
# do calculation
# give me top 3 return options
# plot the graph

inFile = open("callNXPI.csv", "r+")
read = csv.reader(inFile)
write = csv.writer(inFile)

# read everything including header row
head = next(read)

def getStrikePrice():
    strikePrice = 127.5
    temp = input("Enter strike price (default is 127.5): ")
    if temp:
        return temp
    else:
        return strikePrice

strikePrice = getStrikePrice()
listOfLists = [r for r in read]

# insert merger close price and its header
head.append("targetPrice")
for list in listOfLists:
    list.append(strikePrice)

inFile.close()

# get index of all the things I need using the header
maxMultiple = 0
curStrikePrice = 0
indexOfStrikePrice = head.index("strike")
indexOfAskPrice = head.index("ask")
indexOfTargetPrice = head.index("targetPrice")

# calculate profit

for list in listOfLists:
    strikePrice = float(list[indexOfStrikePrice])
    # print("Strike price " + str(strikePrice))
    profitPerOption = float(list[indexOfTargetPrice]) - strikePrice

    # option price = ask price
    optionAskPrice = float(list[indexOfAskPrice])

    # division by 0
    if(optionAskPrice == 0):
        continue

    profitAfterOptionPrice = profitPerOption - optionAskPrice
    returnMultiple = profitAfterOptionPrice / optionAskPrice

    list.append(profitAfterOptionPrice)
    list.append(returnMultiple)

headerReturnMultiple = "returnMultiple"
head.append("profit")
head.append(headerReturnMultiple)

# sort based on returnMultiple
listOfLists.sort(key=itemgetter(
    head.index(headerReturnMultiple)), reverse=True)

print("Top 5 return options: ")
for i in range(0, 5):
    print("Multiple: \t\t" +
          str(listOfLists[i][head.index(headerReturnMultiple)]))
    print("Strike price: \t\t" + str(listOfLists[i][head.index("strike")]))
    print("Profit: \t\t" + str(listOfLists[i][head.index("profit")]))

inFile = open("csvCalculatedOption.csv", "w")
writer = csv.writer(inFile)
writer.writerow(head)
for list in listOfLists:
    writer.writerow(list)
inFile.close()
# print(listOfLists)

