import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


# resample : randomly select an element from the original array and stored in new array, repeat the process
#			(so the new array can have the same element more than once)
#			
# bootstrap sample = A resampled arrey of the data
# bootstrap replicate : A statistic computed from a resampled array
#
# Then if we have a lot of bootstrap samples we can look at the pdf of the statistic ( e.g. pdf of the mean) of the data.
#
# If we have a data set with n repeated measurements, a bootstrap sample is an array of length n that was drawn from the original data with replacement.
#
# A bootstrap replicate is a single value of a statistic computed from a bootstrap sample.


def ecdf(data):
	"""Compute ECDF for a one-dimensional array of measurements."""
	# Number of data points: n
	n = len(data)
	
	# x-data for the ECDF: x
	x = np.sort(data)
	
	# y-data for the ECDF: y
	y = np.arange(1, n+1) / float(n)
	# The y data of the ECDF go from 1/n to 1 in equally spaced increments. You can construct this using np.arange(). Remember, however, that the end value in np.arange() is not inclusive. Therefore, np.arange() will need to go from 1 to n+1. Be sure to divide this by n
	return x, y


# Set default Seaborn style
sns.set()

##---------------------------------
## Visualizing bootstrap samples
##---------------------------------

# In this exercise, you will generate bootstrap samples from the set of annual rainfall data measured at the Sheffield Weather Station in the UK from 1883 to 2015. The data are stored in the NumPy array rainfall in units of millimeters (mm). By graphically displaying the bootstrap samples with an ECDF, you can get a feel for how bootstrap sampling allows probabilistic descriptions of data.

rainfall = np.array([ 875.5,  648.2,  788.1,  940.3,  491.1,  743.5,  730.1,  686.5,
	   878.8,  865.6,  654.9,  831.5,  798.1,  681.8,  743.8,  689.1,
	   752.1,  837.2,  710.6,  749.2,  967.1,  701.2,  619. ,  747.6,
	   803.4,  645.6,  804.1,  787.4,  646.8,  997.1,  774. ,  734.5,
	   835. ,  840.7,  659.6,  828.3,  909.7,  856.9,  578.3,  904.2,
	   883.9,  740.1,  773.9,  741.4,  866.8,  871.1,  712.5,  919.2,
	   927.9,  809.4,  633.8,  626.8,  871.3,  774.3,  898.8,  789.6,
	   936.3,  765.4,  882.1,  681.1,  661.3,  847.9,  683.9,  985.7,
	   771.1,  736.6,  713.2,  774.5,  937.7,  694.5,  598.2,  983.8,
	   700.2,  901.3,  733.5,  964.4,  609.3, 1035.2,  718. ,  688.6,
	   736.8,  643.3, 1038.5,  969. ,  802.7,  876.6,  944.7,  786.6,
	   770.4,  808.6,  761.3,  774.2,  559.3,  674.2,  883.6,  823.9,
	   960.4,  877.8,  940.6,  831.8,  906.2,  866.5,  674.1,  998.1,
	   789.3,  915. ,  737.1,  763. ,  666.7,  824.5,  913.8,  905.1,
	   667.8,  747.4,  784.7,  925.4,  880.2, 1086.9,  764.4, 1050.1,
	   595.2,  855.2,  726.9,  785.2,  948.8,  970.6,  896. ,  618.4,
	   572.4, 1146.4,  728.2,  864.2,  793. ])


for i in range(50):
	# Generate bootstrap sample: bs_sample
	bs_sample = np.random.choice(rainfall, size=len(rainfall))
		
	# Compute and plot ECDF from bootstrap sample
	x, y = ecdf(bs_sample)
	_ = plt.plot(x, y, marker='.', linestyle='none',color='gray', alpha=0.1)

# Compute and plot ECDF from original data
x, y = ecdf(rainfall)
_ = plt.plot(x, y, marker='.')

# Make margins and label axes
plt.margins(0.02)
_ = plt.xlabel('yearly rainfall (mm)')
_ = plt.ylabel('ECDF')

# Show the plot
plt.show()

# Notice how the bootstrap samples give an idea of how the distribution of rainfalls is spread.

##---------------------------------
## Generating many bootstrap replicates
##---------------------------------

def bootstrap_replicate_1d(data, func):
	return func(np.random.choice(data, size=len(data)))

def draw_bs_reps(data, func, size=1):
	"""Draw bootstrap replicates."""
	# Initialize array of replicates: bs_replicates
	bs_replicates = np.empty(size)

	# Generate replicates
	for i in range(size):
		bs_replicates[i] = bootstrap_replicate_1d(data, func)

	return bs_replicates

##---------------------------------
## Bootstrap replicates of the mean and the SEM (standard error of the mean)
##---------------------------------

# Take 10,000 bootstrap replicates of the mean: bs_replicates
bs_replicates = draw_bs_reps(rainfall, np.mean, 10000)

# Compute and print SEM
sem = np.std(rainfall) / np.sqrt(len(rainfall))
print(sem)

# Compute and print standard deviation of bootstrap replicates
bs_std = np.std(bs_replicates)
print(bs_std)

# Make a histogram of the results
_ = plt.hist(bs_replicates, bins=50, normed=True)
_ = plt.xlabel('mean annual rainfall (mm)')
_ = plt.ylabel('PDF')

# Show the plot
plt.show()

# Notice that the SEM we got from the known expression and the bootstrap replicates is the same and the distribution of the bootstrap replicates of the mean is Normal.

##---------------------------------
## Confidence intervals of rainfall data
##---------------------------------

# A confidence interval gives upper and lower bounds on the range of parameter values you might expect to get if we repeat our measurements. For named distributions, you can compute them analytically or look them up, but one of the many beautiful properties of the bootstrap method is that you can take percentiles of your bootstrap replicates to get your confidence interval. Conveniently, you can use the np.percentile() function.

# This means you can use bootstrap method to find Confidence intervals without knowing the type of PDF of your staistic (e.g. mean) !!!

# Use the bootstrap replicates you just generated to compute the 95% confidence interval. That is, give the 2.5th and 97.5th percentile of your bootstrap replicates stored as bs_replicates
np.percentile(bs_replicates, [2.5,97.5])
print np.percentile(bs_replicates, [2.5,97.5])

##---------------------------------
## Bootstrap replicates of other statistics
##---------------------------------
# We saw in a previous exercise that the mean is Normally distributed. This does not necessarily hold for other statistics, but no worry: as hackers, we can always take bootstrap replicates! In this exercise, you'll generate bootstrap replicates for the variance of the annual rainfall at the Sheffield Weather Station and plot the histogram of the replicates.

# Generate 10,000 bootstrap replicates of the variance: bs_replicates
bs_replicates = draw_bs_reps(rainfall, np.var, 10000)

# Put the variance in units of square centimeters
bs_replicates = bs_replicates/100

# Make a histogram of the results
_ = plt.hist(bs_replicates, bins=50, normed=True)
_ = plt.xlabel('variance of annual rainfall (sq. cm)')
_ = plt.ylabel('PDF')

# Show the plot
plt.show()
# This is not normally distributed, as it has a longer tail to the right. Note that you can also compute a confidence interval on the variance, or any other statistic, using np.percentile() with your bootstrap replicates.
print np.percentile(bs_replicates, [2.5,97.5])




##---------------------------------
## Confidence interval on the rate of no-hitters
##---------------------------------
# Consider again the inter-no-hitter intervals for the modern era of baseball. Generate 10,000 bootstrap replicates of the optimal parameter τ. Plot a histogram of your replicates and report a 95% confidence interval.
# Recall that the the optimal \tau is calculated as the mean of the data

nohitter_times = np.array([ 843, 1613, 1101,  215,  684,  814,  278,  324,  161,  219,  545,
						   715,  966,  624,   29,  450,  107,   20,   91, 1325,  124, 1468,
						   104, 1309,  429,   62, 1878, 1104,  123,  251,   93,  188,  983,
						   166,   96,  702,   23,  524,   26,  299,   59,   39,   12,    2,
						   308, 1114,  813,  887,  645, 2088,   42, 2090,   11,  886, 1665,
						   1084, 2900, 2432,  750, 4021, 1070, 1765, 1322,   26,  548, 1525,
						   77, 2181, 2752,  127, 2147,  211,   41, 1575,  151,  479,  697,
						   557, 2267,  542,  392,   73,  603,  233,  255,  528,  397, 1529,
						   1023, 1194,  462,  583,   37,  943,  996,  480, 1497,  717,  224,
						   219, 1531,  498,   44,  288,  267,  600,   52,  269, 1086,  386,
						   176, 2199,  216,   54,  675, 1243,  463,  650,  171,  327,  110,
						   774,  509,    8,  197,  136,   12, 1124,   64,  380,  811,  232,
						   192,  731,  715,  226,  605,  539, 1491,  323,  240,  179,  702,
						   156,   82, 1397,  354,  778,  603, 1001,  385,  986,  203,  149,
						   576,  445,  180, 1403,  252,  675, 1351, 2983, 1568,   45,  899,
						   3260, 1025,   31,  100, 2055, 4043,   79,  238, 3931, 2351,  595,
						   110,  215,    0,  563,  206,  660,  242,  577,  179,  157,  192,
						   192, 1848,  792, 1693,   55,  388,  225, 1134, 1172, 1555,   31,
						   1582, 1044,  378, 1687, 2915,  280,  765, 2819,  511, 1521,  745,
						   2491,  580, 2072, 6450,  578,  745, 1075, 1103, 1549, 1520,  138,
						   1202,  296,  277,  351,  391,  950,  459,   62, 1056, 1128,  139,
						   420,   87,   71,  814,  603, 1349,  162, 1027,  783,  326,  101,
						   876,  381,  905,  156,  419,  239,  119,  129,  467])

# Draw bootstrap replicates of the mean no-hitter time (equal to tau): bs_replicates
bs_replicates = draw_bs_reps(nohitter_times, np.mean, 10000)

# Compute the 95% confidence interval: conf_int
conf_int = np.percentile(bs_replicates, [2.5,97.5])

# Print the confidence interval
print('95% confidence interval =', conf_int, 'games')

# Plot the histogram of the replicates
_ = plt.hist(bs_replicates, bins=50, normed=True)
_ = plt.xlabel(r'$\tau$ (games)')
_ = plt.ylabel('PDF')

# Show the plot
plt.show()

# This gives you an estimate of what the typical time between no-hitters is. It could be anywhere between 660 and 870 games.

