#!/usr/bin/python3

import csv
import sys
from operator import itemgetter

# import csv file
# do calculation
# give me top 3 return options
# plot the graph


def calculateProfit(indexOfStrikePrice, indexOfAskPrice, indexOfTargetPrice, optionList, callsOrPuts):
    for list in optionList:
        strikePrice = float(list[indexOfStrikePrice])
        # print("Strike price " + str(strikePrice))

        profitPerOption = 0
        if(callsOrPuts == "calls"):
            profitPerOption = float(list[indexOfTargetPrice]) - strikePrice
        else:
            profitPerOption = abs(float(list[indexOfTargetPrice]) - strikePrice)

        # option price = ask price
        optionAskPrice = float(list[indexOfAskPrice])

        # division by 0
        if(optionAskPrice == 0):
            continue

        profitAfterOptionPrice = profitPerOption - optionAskPrice
        returnMultiple = profitAfterOptionPrice / optionAskPrice

        list.append(profitAfterOptionPrice)
        list.append(returnMultiple)


def main(targetPrice, callsOrPuts):
    inFile = open("callNXPI.csv", "r+")
    read = csv.reader(inFile)

    # read everything including header row
    head = next(read)

    listOfLists = [r for r in read]

    # insert merger close price and its header
    head.append("targetPrice")
    for list in listOfLists:
        list.append(targetPrice)

    inFile.close()

    # get index of all the things I need using the header
    indexOfStrikePrice = head.index("strike")
    indexOfAskPrice = head.index("ask")
    indexOfTargetPrice = head.index("targetPrice")

    # calculate profit

    calculateProfit(indexOfStrikePrice, indexOfAskPrice,
                    indexOfTargetPrice, listOfLists, callsOrPuts)

    headerReturnMultiple = "returnMultiple"
    head.append("profit")
    head.append(headerReturnMultiple)

    # sort based on returnMultiple
    listOfLists.sort(key=itemgetter(
        head.index(headerReturnMultiple)), reverse=True)

    print("Top return options: ")
    optionsToPrint = 3
    if(len(listOfLists) < optionsToPrint):
        optionsToPrint = len(listOfLists)
    for i in range(0, optionsToPrint):
        print("Multiple: \t".rjust(30) +
              str(listOfLists[i][head.index(headerReturnMultiple)]))
        print("Strike price: \t".rjust(30) +
              str(listOfLists[i][head.index("strike")]))
        print("Profit: \t".rjust(30) +
              str(listOfLists[i][head.index("profit")]))
        print("Option ask price: \t".rjust(30) +
              str(listOfLists[i][head.index("ask")]))
        print('\n')

    inFile = open("csvCalculatedOption.csv", "w")
    writer = csv.writer(inFile)
    writer.writerow(head)
    for list in listOfLists:
        writer.writerow(list)
    inFile.close()
    # print(listOfLists)


if __name__ == "__main__":
    main(127.5, "calls")
