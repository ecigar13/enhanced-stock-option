#!/usr/bin/python3
import changeCsvOptionTable
import fetchOptionTable
import sys

#example usage: python3 enhanced-stock-option.py NXPI y 0 127.5


print(sys.argv)
ticker = sys.argv[1]
showStockQuoteBoolean = sys.argv[2]
dateChoice = sys.argv[3]
targetPrice = sys.argv[4]


fetchOptionTable.main(ticker, showStockQuoteBoolean,dateChoice)
changeCsvOptionTable.main(targetPrice)