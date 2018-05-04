import json
import urllib.request
import urllib
import csv
import time
import datetime, requests

optionUrl = "https://query1.finance.yahoo.com/v7/finance/options/"

## Get stock symbol

def setStockName(optionUrl):
    stockName = "NXPI"
    temp = input("Enter stock symbol: ")
    if(len(temp)):
        stockName = temp
    newOptionLink = optionUrl + stockName
    #print(newOptionLink)
    return newOptionLink

linkNoDate = setStockName(optionUrl)

## Append expiration date
## No expiration date means we just don't use this method
def setExpirationDate(newOptionLink):
    optionUrlWithDate = newOptionLink + "?date="  # linux date
    now = datetime.datetime.now().replace(microsecond=0).timestamp()
    optionUrlWithDate = optionUrlWithDate + str(now)[:-2]
    #print(optionUrlWithDate)
    return optionUrlWithDate

linkWDate=setExpirationDate(linkNoDate)

## Get Json file
def getJsonGetMethod(urlLink):
    tempJson = requests.get(urlLink).json()
    #print(tempJson)
    return tempJson

def getJsonLoadMethod(urlLink):
    response = response = urllib.request.urlopen(urlLink)
    stringResponse = response.read().decode('utf-8')
    jsonFile = json.loads(stringResponse)
    #print(jsonFile)
    return jsonFile

jsonNoDate = getJsonGetMethod(linkNoDate)
jsonWDate = getJsonLoadMethod(linkWDate)

#put json into csv, see what's in it.

#manipulate so I can add formula to it


