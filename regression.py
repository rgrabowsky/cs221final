# Code for linear regression
import csv
import numpy
from sklearn import linear_model

def dotProduct(vec1, vec2):
	result = 1
	for index, val in enumerate(vec1):
		result += val * vec2[index]
	return result


def featureExtractor(dataPoint, features, featuresIndex):
	currencyToFloat = lambda currStr: float(currStr.strip('$').replace(',', ''))
	featureVec = []
	for index, feat in enumerate(features):
		yVal = listing[featuresIndex[index]]
		if feat == 'security_deposit' or feat == 'cleaning_fee' and yVal != "":
			yVal = yVal[1:]
		yVal = yVal.replace(',', '')
		if yVal == "":
			yVal = 0
		featureVec.append( int(float(yVal)))
	return featureVec


with open('./data/nyc-listings.csv', 'rb') as csvfile:
	reader = csv.reader(csvfile)
	data = list(reader)
	headers = data[0]
	features = ['accommodates', 'bathrooms', 'bedrooms', 'beds', 'guests_included', 'security_deposit', 'cleaning_fee']
	featuresIndex = [headers.index(feat) for feat in features]
	
	# Randomize order of rows in data before doing this
	testData = data[1:1001]
	learningData = data[1001:]
	featureVectors = []
	yValueVector = []
	yValueIndex = headers.index('price')
	currencyToFloat = lambda currStr: float(currStr.strip('$').replace(',', ''))


	for listing in learningData:
		featureVec = featureExtractor(listing, features, featuresIndex)
		featureVectors.append(featureVec)
		yValueVector.append( currencyToFloat(listing[yValueIndex]) )

	lm = linear_model.LinearRegression()
	lm.fit(featureVectors, yValueVector)
	
	#Testing
	diffs = []
	NUM_OF_PRINTED_SAMPLES = 10

	print "%s test samples printed out of %s \n" % (NUM_OF_PRINTED_SAMPLES, len(testData))
	for index, listing in enumerate(testData):
		
		featureVec = featureExtractor(listing, features, featuresIndex)
		estimatedPrice = dotProduct(featureVec, lm.coef_)
		actualPrice = listing[yValueIndex]
		diff = abs(estimatedPrice - currencyToFloat(actualPrice))
		diffs.append(diff)

		if index < NUM_OF_PRINTED_SAMPLES:
			print "Feature vector: %s" % featureVec
			estimatedPriceString = "$" + str(round(estimatedPrice, 2))
			print "Estimated Price: %s" % estimatedPriceString
			print "Actual Price: %s \n" % actualPrice

	print "Average differential: %s" % "$" + str(round(numpy.mean(diffs), 2))
