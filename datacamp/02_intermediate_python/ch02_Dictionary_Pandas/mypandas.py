import pandas as pd

if False:
	# Pre-defined lists
	names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
	dr =  [True, False, False, False, True, True, True]
	cpc = [809, 731, 588, 18, 200, 70, 45]

	# Import pandas as pd
	#import pandas as pd

	# Create dictionary my_dict with three key:value pairs: my_dict
	my_dict = {
		'country':names,
			'drives_right':dr,
				'cars_per_cap':cpc
	}

	# Build a DataFrame cars from my_dict: cars
	cars = pd.DataFrame(my_dict)

	# Print cars
	print (cars)

	# Definition of row_labels
	row_labels = ['US', 'AUS', 'JAP', 'IN', 'RU', 'MOR', 'EG']

	# Specify row labels of cars
	cars.index = row_labels

	# Print cars again
	print(cars)


if False:
	##Putting data in a dictionary and then building a DataFrame works, but it's not very efficient. What if you're dealing with millions of observations? In those cases, the data is typically available as files with a regular structure. One of those file types is the CSV file, which is short for "comma-separated values".

	# Import the cars.csv data: cars
	# https://raw.githubusercontent.com/wblakecannon/DataCamp/master/02-intermediate-python-for-data-science/_datasets/cars.csv
	#cars = pd.read_csv('cars.csv')
	
	# Fix import by including index_col
	cars = pd.read_csv('cars.csv',index_col=0)

	# Print out cars
	print(cars)
	print (' >> new line')


if False:
	## using bracket [], [[]]
	cars = pd.read_csv('cars.csv',index_col=0)
	
	# Print out country column as Pandas Series
	print (cars['country'])
	print (' >> new line')
	print (type(cars['country']))
	print (' >> new line')
	
	# Print out country column as Pandas DataFrame
	print (cars[['country']])
	print (' >> new line')
	print (type(cars[['country']]))
	print (' >> new line')

	# Print out DataFrame with country and drives_right columns
	print (cars[['country','drives_right']])


if False:
	## using slicing
	cars = pd.read_csv('cars.csv', index_col = 0)

	# Print out first 3 observations
	print(cars[0:3])
	print(type(cars[0:3]))

	# Print out fourth, fifth and sixth observation
	#print(cars[3:6])


if False:
	## using loc, iloc
	cars = pd.read_csv('cars.csv', index_col = 0)

	# Print out observation for Japan, Make sure to print the resulting Series.
	print(cars.loc['JAP'])
	print(cars.iloc[2])
	#print(cars.loc[['JAP']])
	#print(cars.iloc[[2]])
	
	# Print out observations for Australia and Egypt,  Make sure to print the resulting DataFrame.
	print(cars.loc[['AUS','EG']])
	print(cars.iloc[[1,6]])


if False:
	## using loc, iloc to access both row and col
	cars = pd.read_csv('cars.csv', index_col = 0)


	cars.loc['IN', 'cars_per_cap']
	cars.iloc[3, 0]

	cars.loc[['IN', 'RU'], 'cars_per_cap']
	cars.iloc[[3, 4], 0]

	cars.loc[['IN', 'RU'], ['cars_per_cap', 'country']]
	cars.iloc[[3, 4], [0, 1]]

	# Print out drives_right value of Morocco
	print(cars.loc['MOR','drives_right'])

	# Print sub-DataFrame
	print(cars.loc[['RU','MOR'],['country','drives_right']])


if True:
	## using loc, iloc to access entire col
	cars = pd.read_csv('cars.csv', index_col = 0)

	cars.loc[:, 'country']
	cars.iloc[:, 1]

	print(cars.loc[:, ['country']])

	cars.loc[:, ['country','drives_right']]
	cars.iloc[:, [1, 2]]


	# Print out drives_right column as Series
	print(cars.loc[:,'drives_right'])


	# Print out drives_right column as DataFrame
	print(cars.loc[:,['drives_right']])

	# Print out cars_per_cap and drives_right as DataFrame
	print(cars.loc[:,['cars_per_cap','drives_right']])






























































