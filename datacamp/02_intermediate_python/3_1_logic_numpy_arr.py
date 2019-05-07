### Chapter 3


if False:
	## Numpy Recap
	import numpy as np

	# create Numpy array from a list
	np_height = np.array([1.73, 1.68, 1.71, 1.89, 1.79])
	mp_weight = np.array([65.4, 59.2, 63.6, 88.4, 68.7])

	# we can do element-wise operation
	bmi = mp_weight/(np_height ** 2)
	print (bmi)

	# create array of boolean
	print (bmi>23)
	#print (type(bmi>23))

	# use array of boolean as a selection
	print (bmi[bmi>23])
	#print ( type(bmi[bmi>23]) )


if False:
	print ('carl' < 'chris')
	print (3 < 4)
	print (3 < 'chris') # make sure you understand this # depend on python version?

	# Comparison of booleans
	print (True == False)

	# Comparison of integers
	print (-5 * 15 != 75)

	# Comparison of strings
	print ('pyscript' == 'PyScript')

	# Compare a boolean with an integer
	print (True == 1)

	# Comparison of integers
	x = -3 * 6
	print (x >= -10)

	# Comparison of strings
	y = "test"
	print ('test' <= y)

	# Comparison of booleans
	print (True > False)


if False:
	## Compare arrays

	## Remember areas, the list of area measurements for different rooms in your house from the previous course? This time there's two Numpy arrays: my_house and your_house. They both contain the areas for the kitchen, living room, bedroom and bathroom in the same order, so you can compare them.

	import numpy as np
	my_house = np.array([18.0, 20.0, 10.75, 9.50])
	your_house = np.array([14.0, 24.0, 14.25, 9.0])

	# my_house greater than or equal to 18
	print (my_house >= 18)

	# my_house less than your_house
	print (my_house < your_house)



if False:
	## Numpy array comparison & bool operation
	import numpy as np
	
	# create Numpy array from a list
	np_height = np.array([1.73, 1.68, 1.71, 1.89, 1.79])
	mp_weight = np.array([65.4, 59.2, 63.6, 88.4, 68.7])
	
	# we can do element-wise operation
	bmi = mp_weight/(np_height ** 2)
	print (bmi)
	
	# create array of boolean
	print (bmi>23)
	#print (type(bmi>23))
	
	# use array of boolean as a selection
	print (bmi[bmi>23])
	#print ( type(bmi[bmi>23]) )

	## --------------------------
	# create array of boolean
	print (bmi>21)

	# create array of boolean
	print (bmi<22)

	# doing element-wise bool operation
	#print ( bmi>21 and bmi<22) ## this does not work
	
	## we have to use >>  logical_and, logical_or, logical_not
	print ( np.logical_and(bmi>21, bmi<22) )

	# we can, again, use this array of boolean as a condition for selection
	print ( bmi[np.logical_and(bmi>21, bmi<22)] )


if False:

	### Boolean operators with Numpy
	### Before, the operational operators like < and >= worked with Numpy arrays out of the box. Unfortunately, this is not true for the boolean operators and, or, and not.
	### To use these operators with Numpy, you will need np.logical_and(), np.logical_or() and np.logical_not(). Here's an example on the my_house and your_house arrays from before to give you an idea:

	# Create arrays
	import numpy as np
	my_house = np.array([18.0, 20.0, 10.75, 9.50])
	your_house = np.array([14.0, 24.0, 14.25, 9.0])

	# my_house greater than 18.5 or smaller than 10
	print ( my_house>18.5 )
	print ( my_house<10 )
	print ( np.logical_or(my_house>18.5,my_house<10) )

	# Both my_house and your_house smaller than 11
	print (" ")
	print ( my_house<11 )
	print ( your_house<11 )
	print ( np.logical_and(my_house<11,your_house<11) )


if True:
	import numpy as np
	# how about 2-d array ==> matrix
	a1d = np.array([3,33,333])
	print a1d
	print type(a1d)
	print a1d.shape
	print a1d[0], a1d[1], a1d[2]

	b2d = np.array([[11,12,13],[21,22,23]])
	print b2d
	print type(b2d)
	print b2d.shape
	print ' to access elements >> b2d[0,0]'
	print b2d[0,0],b2d[0,1],b2d[0,2]
	print b2d[1,0],b2d[1,1],b2d[1,2]
	print ' another way to access elements >> b2d[0][0]'
	print b2d[0][0],b2d[0][1],b2d[0][2]
	print b2d[1][0],b2d[1][1],b2d[1][2]



































