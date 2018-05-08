import csv

inFile = open("callNXPI.csv", "r+")
read = csv.reader(inFile)
write = csv.writer(inFile)

strikePrice = 127.5
# skip header row
next(read)   

data = [r for r in read]
for item in data:
    data.insert(strikePrice,0)

print(data[0])
#import csv file

#do calculation

#give me top 3 return options

#plot the graph