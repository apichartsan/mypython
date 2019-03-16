###	Chapter 3
###		>> Filtering Pandas DataFrame


if False:
	import pandas as pd
	
	#brics = pd.read_csv("brics.csv")
	brics = pd.read_csv("brics.csv", index_col = 0)
	print brics, '\n'

	# Goal: select countries with area over 8 million km2
	# 3 steps
	# (1) select the area column >> need the result in pandas series (not  dataframe)
	# (2) do comparison on area column and store results >> in pandas series
	# (3) Use the results to do selection on dataframe

	#print brics['area']		# pandas series
	#print brics['area']>8
	is_huge = brics['area']>8 # pandas series of boolean

	#brics_area_gr8 = brics[is_huge] # dataframe
	brics_area_gr8 = brics[brics['area']>8] # do it in 1 line
	print brics_area_gr8, '\n'


	## Goal: combine conditions using numpy boolean operators
	##  np.logical_and(), np.logical_or() and np.logical_not()
	## >> numpy allow for the element-wised operation
	import numpy as np
	
	brics_new = brics[ np.logical_and(brics['area']>8, brics['area']<10) ] # think of pandas series as numpy array
	print brics_new, '\n'


import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)
print cars
# Extract drives_right column as Series: dr
#dr = cars['drives_right'] == True
# Use dr to subset cars: sel
#sel = cars[dr]

# Convert code to a one-liner
sel = cars[cars['drives_right']]
# Print sel
print (sel)

# Create car_maniac: observations that have a cars_per_cap over 500
car_maniac = cars[cars['cars_per_cap']>500]
# Print car_maniac
print (car_maniac)

# Create medium: observations with cars_per_cap between 100 and 500
cpc = cars['cars_per_cap'] # pandas Series
between = np.logical_and(cpc > 100, cpc < 500)
medium = cars[between]
# Print medium
print (medium)









