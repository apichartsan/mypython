
#while condition :
#	expression

if False:
	error = 50.0
	while error > 1 :
		error = error/4
		print error

if False:
	# Initialize offset
	offset = 8
	# Code the while loop
	while offset != 0 :
		print ('correcting...')
		offset -= 1
		print (offset)

if False:
	# Initialize offset
	offset = -6
	# Code the while loop
	while offset != 0 :
		print("correcting...")
		if offset>0 :
			offset = offset - 1
		elif offset<0 :
			offset = offset + 1
		print(offset)


#for var in seq :
#	expression

if False:
	fam = [1.73, 1.68, 1.71, 1.89, 1.79]
	print fam
	for height in fam:
		print height
	
	## obtain also the index of the list using "enumerate"
	for index, height in enumerate(fam):
		print "index " + str(index) + ": " + str(height)

	for c in "family":
		print c, c.capitalize()


if False:
	# areas list
	areas = [11.25, 18.0, 20.0, 10.75, 9.50]
	# Code the for loop
	for ar in areas:
		print (ar)
	# If you also want to access the index information, so where the list element you're iterating over is located, you can use enumerate().
	# Change for loop to use enumerate() and update print()
	for ind,a in enumerate(areas) :
		print('room '+ str(ind) + ': '+ str(a))


if False:
	# house list of lists
	house = [["hallway", 11.25],
			 ["kitchen", 18.0],
			 ["living room", 20.0],
			 ["bedroom", 10.75],
			 ["bathroom", 9.50]]
	# Build a for loop from scratch
	for r in house:
		print ("the " + str(r[0]) + " is " + str(r[1]) + " sqm")


##--------------------------##
## Loop over dictionary
##--------------------------##
if False:
	# disctionary >> use .item() method
	world = {'afghanistan':30.55,
	'albania':2.77,
	'algeria':39.21}

	print world.items()
	for key, val in world.items():
		print key, val
	for key in world.iterkeys():
		print key, world[key]

	# but note that dictionaries are unordered and any change may result in different indices for all items
	for index, key in enumerate(dict):
		print index, key


if False:
	# Definition of dictionary
	europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin',
		'norway':'oslo', 'italy':'rome', 'poland':'warsaw', 'austria':'vienna' }

	# Iterate over europe
	for key, val in europe.items():
		print ("the capital of ", key, " is ", val)
	# Notice that the order of the printouts doesn't necessarily correspond with the order used when defining europe. Remember: dictionaries are inherently unordered!


##--------------------------##
## Loop over numpy array
##--------------------------##

# 1D array
if False:
	import numpy as np
	np_height = np.array([1.73, 1.68, 1.71, 1.89, 1.79])
	for x in np_height :
		print x

# 2D array # use function np.nditer()
if False:
	# np array
	import numpy as np
		
	# create Numpy array from a list
	np_height = np.array([1.73, 1.68, 1.71, 1.89, 1.79])
	mp_weight = np.array([65.4, 59.2, 63.6, 88.4, 68.7])
	meas = np.array([np_height,mp_weight])
	print meas
	for m in meas:
		print m

	# use function np.nditer()
	for val in np.nditer(meas):
		print val

if False:
	# Import numpy as np
	import numpy as np
	np_height = np.array([1.73, 1.68, 1.71, 1.89, 1.79])
	mp_weight = np.array([65.4, 59.2, 63.6, 88.4, 68.7])
	np_baseball = np.array([np_height,mp_weight])
	
	# For loop over np_height
	for x in np_height:
		print x,"inches",

	print ''
	# For loop over np_baseball
	for x in np.nditer(np_baseball):
		print x,







