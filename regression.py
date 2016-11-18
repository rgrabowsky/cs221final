# Code for linear regression
import csv
#from sklearn import linear_model
#reg = linear_model.LinearRegression()


with open('./data/nyc-listings.csv', 'rb') as csvfile:
	reader = csv.reader(csvfile)
	data = list(reader)
	headers = data[0]
	features = ['accommodates', 'bathrooms', 'bedrooms', 'beds', 'guests_included', 'security_deposit', 'cleaning_fee']
	featuresIndex = [headers.index(feat) for feat in features]

	data = data[1:]
	numListings = len(data)
	currencyToFloat = lambda currStr: float(currStr.strip('$').replace(',', ''))
	featureVectors = []

	for listing in data:
		featureVec = []
		for index, feat in enumerate(features):
			yVal = listing[featuresIndex[index]]
			if feat == 'security_deposit' or feat == 'cleaning_fee' and yVal != "":
				yVal = yVal[1:]
			if yVal == "":
				yVal = 0
			featureVec.append( (feat, yVal) )
		featureVectors.append(featureVec)

	print("First data entry: ")
	for index, feat in enumerate(featureVectors[0]):
		print str(feat)

#guests, bathrooms, bedrooms, beds, square feet, 

'''
accomodates: BB
bathrooms: bc
bedrooms: bd
beds: be
security deposit: bl
cleaning fee: bm
number of reviews: by



future
avilabilite
'''