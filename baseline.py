# Write a Python script to find the average price for listings in NYC 
# to get used to working with Excel CSV files in Python
# This is also our BASELINE for the predictor
# Now I need to calculate the accuracy of this baseline
import csv
with open('./data/nyc-listings.csv', 'rb') as csvfile:
	reader = csv.reader(csvfile)
	data = list(reader)
	headers = data[0]
	priceColumnIndex = headers.index('price')
	data = data[1:]
	numListings = len(data)
	print "There are %s rows of listing data" % numListings
	currencyToFloat = lambda currStr: float(currStr.strip('$').replace(',', ''))
	priceSum = sum(currencyToFloat(row[priceColumnIndex]) for row in data)
	avgPrice1 = priceSum / numListings
	avgPrice2 = sum(currencyToFloat(row[priceColumnIndex]) / numListings for row in data)
print "Price sum: %s" % priceSum
print "Average price: {0:.2f}".format(round(avgPrice1, 2)) 
print "Average price: {0:.2f}".format(round(avgPrice2, 2)) 