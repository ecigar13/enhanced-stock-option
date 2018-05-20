#!/usr/bin/python3
import changeCsvOptionTable
import fetchOptionTable
import sys

#example usage: python3 enhanced-stock-option.py NXPI y calls 0 127.5


#need to add: choice of calls/puts option
#add appropriate refractor for calls and puts

print(sys.argv)
ticker = sys.argv[1]
showStockQuoteBoolean = sys.argv[2]
callsOrPuts = sys.argv[3]
dateChoice = sys.argv[4]
targetPrice = sys.argv[5]


fetchOptionTable.main(ticker, callsOrPuts, showStockQuoteBoolean,dateChoice)
changeCsvOptionTable.main(targetPrice, callsOrPuts)
