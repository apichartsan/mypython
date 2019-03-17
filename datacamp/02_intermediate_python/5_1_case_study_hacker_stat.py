#import numpy as np
#import pandas as pd
## Import cars data
#cars = pd.read_csv('cars.csv', index_col = 0)

# Import numpy as np
import numpy as np
# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Set the seed
np.random.seed(123)


if False:
	##----------------------------------##
	##  Random numbers	(float)			##
	##----------------------------------##
	# seed(): sets the random seed, so that your results are the reproducible between simulations. As an argument, it takes an integer of your choosing. If you call the function, no output will be generated.
	# rand(): if you don't specify any arguments, it generates a random float between zero and one.

	# Generate and print random float
	print (np.random.random())


if False:
	##----------------------------------##
	##  Random numbers	(int)			##
	##----------------------------------##
	# Use randint() with the appropriate arguments to randomly generate the integer 1, 2, 3, 4, 5 or 6. This simulates a dice. Print it out.

	# Use randint() to simulate a dice
	print ( np.random.randint(1,7) )

	# Use randint() again
	print ( np.random.randint(1,7) )


if False:
	##----------------------------------##
	##  Determine your next move		##
	##----------------------------------##

	# Numpy is imported, seed is set

	# Starting step
	step = 50

	# Roll the dice
	dice = np.random.randint(1,7)

	# Finish the control construct
	if dice <= 2 :
		step = step - 1
	elif dice in [3,4,5] :
		step = step + 1
	else :
		step = step + np.random.randint(1,7)

	# Print out dice and step
	print (dice, step)


if False:
	##----------------------------------##
	##  one single random_walk			##
	##----------------------------------##
	# Numpy is imported, seed is set

	# Initialize random_walk
	random_walk = [0]

	for x in range(100) :
		# Set step: last element in random_walk
		step = random_walk[-1]
			
		# Roll the dice
		dice = np.random.randint(1,7)

		# Determine next step
		if dice <= 2:
			#step = step - 1 #
			# Replace below: use max() to make sure step can't go below 0
			step = max(0, step - 1)
		elif dice <= 5:
			step = step + 1
		else:
			step = step + np.random.randint(1,7)
		
		# append next_step to random_walk
		random_walk.append(step)

	# Print random_walk
	print (random_walk) # #There's still something wrong: the level at index 15 is negative!

	# Plot random_walk
	plt.plot(random_walk)

	# Show the plot
	plt.show()


if True:
	##----------------------------------##
	##  Visualize all walks				##
	##   >> Implement clumsiness		##
	##   >> Plot the distribution		##
	##----------------------------------##

	# numpy and matplotlib imported, seed set.

	# initialize and populate all_walks
	all_walks = []
	for i in range(500) :
		random_walk = [0]
		for x in range(100) :
			step = random_walk[-1]
			dice = np.random.randint(1,7)
			if dice <= 2:
				step = max(0, step - 1)
			elif dice <= 5:
				step = step + 1
			else:
				step = step + np.random.randint(1,7)
			# Implement clumsiness
			if np.random.rand() <= 0.001 :
				step = 0
			
			random_walk.append(step)
		all_walks.append(random_walk)

	# Convert all_walks to Numpy array: np_aw
	np_aw = np.array(all_walks)

	# Plot np_aw and show
	#_ = plt.plot(np_aw)
	#plt.show()
	# Clear the figure
	#plt.clf()

	# Transpose np_aw: np_aw_t
	np_aw_t =  np.transpose(np_aw)

	# Plot np_aw_t and show
	_ = plt.plot(np_aw_t)
	plt.show()

	# Select last row from np_aw_t: ends
	ends = np_aw_t[-1,:]

	# Plot histogram of ends, display plot
	_ = plt.hist(ends)
	plt.show()

	# Good job! You can clearly see how the different simulations of the random walk went. Transposing the 2D Numpy array was crucial; otherwise Python misunderstood

	# Look at the plot. In some of the 250 simulations you're indeed taking a deep dive down!

#np.count_nonzero(ends >= 60)/float(len(ends))
print np.sum(ends >= 60)/float(len(ends))
# 0.784














