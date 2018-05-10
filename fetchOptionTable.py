import json
import urllib.request
import urllib
import csv
import time
import datetime
import requests

'''
How the yahoo link behave: it needs a stock option after the next link.
If no date is provided, it will return a JSON file with a list of dates
for all available options (usually up until 2020). Below that is other
information about the stock and a list of call AND put options for the
most recent expiration date, usually the coming Friday.)

If the date in the link is invalid (not among the dates that appear in the JSON file,
then the call and put option is empty ([]). This will cause the second half of this .py
file to fail. I will deal with it later.
'''

# Get stock symbol, NXPI by default


def setStockName(optionUrl):
    stockName = "NXPI"
    temp = input("Enter stock symbol (default is NXPI): ")
    if(len(temp)):
        stockName = temp
    newOptionLink = optionUrl + stockName
    # print(newOptionLink)
    return newOptionLink


# Get Json file as a dict


def getJsonGetMethod(urlLink):
    jsonFile = requests.get(urlLink).json()
    # print(jsonFile)
    return jsonFile


def getJsonLoadMethod(urlLink):
    response = response = urllib.request.urlopen(urlLink)
    stringResponse = response.read().decode('utf-8')
    jsonFile = json.loads(stringResponse)
    # print(jsonFile)
    return jsonFile


def extractExpirationDateList(jsonDateList):
    return jsonDateList["optionChain"]["result"][0]["expirationDates"]

# takes in a list of timestamp (int) and return a timestamp (int). The result can be appended to the URL and then sent to Yahoo


def pickDate(availableDatesList):
    index = 0
    for timestamp in availableDatesList:
        printString = str(index) + ":\t" + datetime.datetime.fromtimestamp(
            int(timestamp)).strftime("%A %B %d \t%Y %H %Z")
        index += 1
        print(printString)

    dateChoice = 0
    temp = input(
        "Choose a number from the list (default is 0, the closest option date): ")
    if(temp):
        dateChoice = temp
    return availableDatesList[int(dateChoice)]


# takes in a link with stock symbol and append the timestamp to it


def setExpirationDate(linkNoDate, timestamp):
    return linkNoDate + "?date=" + str(timestamp)


def main():

    optionUrl = "https://query1.finance.yahoo.com/v7/finance/options/"

    # feed the URL with stock name to get available dates for the option
    linkNoDate = setStockName(optionUrl)
    jsonDateList = getJsonGetMethod(linkNoDate)
    # extract the date list from JSON file
    availableDatesList = extractExpirationDateList(jsonDateList)

    stockInfo = jsonDateList["optionChain"]["result"][0]["quote"]
    showStockInfo = 0
    showStockInfo = input("Should I show stock info? (default is no): ")

    if(showStockInfo):
        for key, value in stockInfo.items():
            print('{:30}'.format(str(key)) + " : " + '{:>15}'.format(str(value)))

    # pick a date from the list and add it to the previous URL
    timestamp = pickDate(availableDatesList)
    linkWDate = setExpirationDate(linkNoDate, timestamp)

    # get JSON object from the link. Type is dict
    jsonWDate = getJsonLoadMethod(linkWDate)

    # extract the list of options from the JSON object
    callOptions = jsonWDate["optionChain"]["result"][0]["options"][0]["calls"]
    if not callOptions:
        print("JSON is empty. Please try another option date")
        exit()

    f = open("callNXPI.csv", "w+")

    # write the header and the options to CSV file.
    headers = []
    wr = csv.DictWriter(f, headers)

    if(callOptions != None):
        option = callOptions[0]
        for key, value in option.items():
            headers.append(key)
            # wr.writerow(value)

    wr.writeheader()

    # append the values to an array, then append the array to files.
    wr = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
    for option in callOptions:
        # print(option)
        row = []
        # print(type(row))
        for key, value in option.items():
            # print(type(key), type(value))
            row.append(value)
        wr.writerow(row)

    f.close()

    # this writes to csv file, but for some reasons I don't know, the order of the columns are messed up


main()
