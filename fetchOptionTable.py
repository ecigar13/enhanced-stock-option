import json
import urllib.request
import urllib
import csv
import time
import datetime
import requests

optionUrl = "https://query1.finance.yahoo.com/v7/finance/options/"

# Get stock symbol
def setStockName(optionUrl):
    stockName = "NXPI"
    temp = input("Enter stock symbol: ")
    if(len(temp)):
        stockName = temp
    newOptionLink = optionUrl + stockName
    # print(newOptionLink)
    return newOptionLink


linkNoDate = setStockName(optionUrl)

# Append expiration date
# No expiration date means we just don't use this method
def setExpirationDate(newOptionLink):
    optionUrlWithDate = newOptionLink + "?date="  # linux date
    now = datetime.datetime.now().replace(microsecond=0).timestamp()
    optionUrlWithDate = optionUrlWithDate + str(now)[:-2]
    # print(optionUrlWithDate)
    return optionUrlWithDate


linkWDate = setExpirationDate(linkNoDate)

# Get Json file as a dict
def getJsonGetMethod(urlLink):
    tempJson = requests.get(urlLink).json()
    # print(tempJson)
    return tempJson

def getJsonLoadMethod(urlLink):
    response = response = urllib.request.urlopen(urlLink)
    stringResponse = response.read().decode('utf-8')
    jsonFile = json.loads(stringResponse)
    # print(jsonFile)
    return jsonFile

#get JSON object from the link. Type is dict
jsonNoDate = getJsonGetMethod(linkNoDate)
jsonWDate = getJsonLoadMethod(linkWDate)

#return a list from JSON dict
callOptions = jsonNoDate["optionChain"]["result"][0]["options"][0]["calls"]
#print(callOptions)



f = open("callNXPI.csv", "w+")

#write the header of CSV file
headers = []
wr=csv.DictWriter(f,headers)
if(callOptions != None):
    option = callOptions[0]
    for key, value in option.items():
        headers.append(key)
        #wr.writerow(value)

wr.writeheader()


#append the values to an array, then append the array to files.
wr = csv.writer(f,quoting=csv.QUOTE_NONNUMERIC)
for option in callOptions:
    #print(option)
    row = []
    #print(type(row))
    for key, value in option.items():
        #print(type(key), type(value))
        row.append(value)
    wr.writerow(row)

f.close()
# put json into csv, see what's in it.
# manipulate so I can add formula to it
