import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
#import ROOT
from ROOT import *
import array as arr

# Create bee swarm plot with Seaborn's default settings
sns.set()

def ecdf(data):
	"""Compute ECDF for a one-dimensional array of measurements."""
	""" Empirical Cumulative Distribution Function """
	# Number of data points: n
	n = len(data)

	# x-data for the ECDF: x
	x = np.sort(data)
		
	# y-data for the ECDF: y
	y = np.arange(1, n+1) / float(n)
	# The y data of the ECDF go from 1/n to 1 in equally spaced increments. You can construct this using np.arange(). Remember, however, that the end value in np.arange() is not inclusive. Therefore, np.arange() will need to go from 1 to n+1. Be sure to divide this by n
	return x, y


df = pd.read_csv('iris.csv')
df['species'].value_counts()
set  = df['species'] == 'setosa'
vers = df['species'] == 'versicolor'
virg = df['species'] == 'virginica'

setosa_petal_length = df[set]['petal_length']
versicolor_petal_length = df[vers]['petal_length']
virginica_petal_length = df[virg]['petal_length']

versicolor_petal_width = df[vers]['petal_width']

# Compute ECDFs
x_set, y_set = ecdf(setosa_petal_length)
x_vers, y_vers = ecdf(versicolor_petal_length)
x_virg, y_virg = ecdf(virginica_petal_length)


##---------------------------------
##  mean median
##---------------------------------
# Compute the mean: mean_length_vers
mean_length_vers = np.mean(versicolor_petal_length)
median_length_vers = np.median(versicolor_petal_length)

# Print the result with some nice formatting
print('I. versicolor:', mean_length_vers, 'cm')
print('I. versicolor:', median_length_vers, 'cm')


##---------------------------------
##  percentiles
##---------------------------------
# Specify array of percentiles: percentiles
percentiles = np.array([2.5, 25, 50, 75, 97.5])

# Compute percentiles: ptiles_vers
ptiles_vers = np.percentile(versicolor_petal_length, percentiles)

# Print the result
print (ptiles_vers)

# Plot the ECDF
_ = plt.plot(x_vers, y_vers, '.')
_ = plt.xlabel('petal length (cm)')
_ = plt.ylabel('ECDF')

# Overlay percentiles as red diamonds.
_ = plt.plot(ptiles_vers, percentiles/100, marker='D', color='red',
			 linestyle='none')

# Show the plot
plt.show()


##---------------------------------
##  Box-and-whisker plot
##---------------------------------
# Create box plot with Seaborn's default settings
sns.set()
_ = sns.boxplot(x='species', y='petal_length', data=df)
# Label the axes
_ = plt.xlabel('species')
_ = plt.ylabel('petal length (cm)')

# Show the plot
plt.show()


##---------------------------------
##  Variance and stdev
##---------------------------------

# Array of differences to mean: differences
differences = versicolor_petal_length - np.mean(versicolor_petal_length)

# Square the differences: diff_sq
diff_sq = differences**2

# Compute the mean square difference: variance_explicit
variance_explicit = np.mean(diff_sq)

# Compute the variance using NumPy: variance_np
variance_np = np.var(versicolor_petal_length)

# Print the results
print (variance_explicit, variance_np)

# Compute the variance: variance
variance = np.var(versicolor_petal_length)

# Print the square root of the variance
print (np.sqrt(variance))

# Print the standard deviation
print (np.std(versicolor_petal_length))


##---------------------------------
##  Covariance and Pearson correlation coefficient
##---------------------------------
# Make a scatter plot
_ = plt.plot(versicolor_petal_length, versicolor_petal_width, marker='.', linestyle='none')

# Label the axes
_ = plt.xlabel('versicolor_petal_length')
_ = plt.ylabel('versicolor_petal_width')

# Show the result
plt.show()

# Compute the covariance matrix: covariance_matrix
covariance_matrix = np.cov(versicolor_petal_length, versicolor_petal_width)
# returns a 2D array where entries [0,1] and [1,0] are the covariances. Entry [0,0] is the variance of the data in x, and entry [1,1] is the variance of the data in y

# Print covariance matrix
print (covariance_matrix)

# Extract covariance of length and width of petals: petal_cov
petal_cov = covariance_matrix[0][1]

# Print the length/width covariance
print(petal_cov)

def pearson_r(x, y):
	"""Compute Pearson correlation coefficient between two arrays."""
	# Compute correlation matrix: corr_mat
	corr_mat = np.corrcoef(x, y)
	# Return entry [0,1]
	return corr_mat[0,1]

# Compute Pearson correlation coefficient for I. versicolor: r
r = pearson_r(versicolor_petal_length, versicolor_petal_width)

# Print the result
print (r)
