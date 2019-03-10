import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
#import ROOT
from ROOT import *
import array as arr

# Create bee swarm plot with Seaborn's default settings
sns.set()

if False:
	# Seed the random number generator
	np.random.seed(42)

	# Initialize random numbers: random_numbers
	random_numbers = np.empty(100000)

	# Generate random numbers by looping over range(100000)
	for i in range(100000):
		random_numbers[i] = np.random.random()

	# Instead of for loop, you can do random_numbers = np.random.random(100000)
	
	# Plot a histogram
	_ = plt.hist(random_numbers)

	# Show the plot
	plt.show()


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

def perform_bernoulli_trials(n, p):
	"""Perform n Bernoulli trials with success probability p
		and return number of successes."""
	# Initialize number of successes: n_success
	n_success = 0

	# Perform trials
	for i in range(n):
		# Choose random number between zero and one: random_number
		random_number = np.random.random()

		# If less than p, it's a success so add one to n_success
		if random_number < p:
			n_success += 1

	return n_success

if False:
	a = perform_bernoulli_trials(100, 0.9)
	print (a)



# Let's say a bank made 100 mortgage loans. It is possible that anywhere between 0 and 100 of the loans will be defaulted upon. You would like to know the probability of getting a given number of defaults, given that the probability of a default is p = 0.05. To investigate this, you will do a simulation. You will perform 100 Bernoulli trials using the perform_bernoulli_trials() function you wrote in the previous exercise and record how many defaults we get. Here, a success is a default. (Remember that the word "success" just means that the Bernoulli trial evaluates to True, i.e., did the loan recipient default?) You will do this for another 100 Bernoulli trials. And again and again until we have tried it 1000 times. Then, you will plot a histogram describing the probability of the number of defaults.

if False:
	# Seed random number generator
	np.random.seed(42)

	# Initialize the number of defaults: n_defaults
	n_defaults = np.empty(1000)

	# Compute the number of defaults
	for i in range(1000):
		n_defaults[i] = perform_bernoulli_trials(100, 0.05)


	# Plot the histogram with default number of bins; label your axes
	_ = plt.hist(n_defaults, normed=True)
	_ = plt.xlabel('number of defaults out of 100 loans')
	_ = plt.ylabel('probability')

	# Show the plot
	plt.show()


# Plot the number of defaults you got from the previous exercise, in your namespace as n_defaults, as a CDF. The ecdf() function you wrote in the first chapter is available.
# If interest rates are such that the bank will lose money if 10 or more of its loans are defaulted upon, what is the probability that the bank will lose money?
if False:
	# Compute ECDF: x, y
	x, y = ecdf(n_defaults)

	# Plot the ECDF with labeled axes
	_ = plt.plot(x, y, marker = '.', linestyle = 'none')
	_ = plt.xlabel ("n_defaults in 100 trials")
	_ = plt.ylabel ("ECDF")

	# Show the plot
	plt.show()

	# Compute the number of 100-loan simulations with 10 or more defaults: n_lose_money
	n_lose_money = np.sum(n_defaults>=10)

	# Compute and print probability of losing money
	print('Probability of losing money =', n_lose_money / len(n_defaults))


##---------------------------------
##  np.random.binomial()
##---------------------------------
## The procedures we did above can be easily done with np.random.binomial()

if False:
	# Take 10,000 samples out of the binomial distribution: n_defaults
	n_defaults = np.random.binomial(100, 0.05, 10000)

	# Compute CDF: x, y
	x, y = ecdf(n_defaults)

	# Plot the CDF with axis labels
	_ = plt.plot(x, y, marker = '.', linestyle = 'none')
	_ = plt.xlabel ("n_defaults in 100 trials")
	_ = plt.ylabel ("ECDF")

	# Show the plot
	plt.show()
	# Now you know that this plot is the cumulative binomial distribution with n =100, p = 0.05


# Although this is discrete distribution, we will just plot histogram, instead of PMF (probability mass function (PMF)— also called a frequency function)
if False:
	# Compute bin edges: bins
	bins = np.arange(0, max(n_defaults) + 1.5) - 0.5

	# Generate histogram
	_ = plt.hist(n_defaults, normed=True, bins=bins)

	# Label axes
	_ = plt.xlabel("n_defaults in 100 trials")
	_ = plt.ylabel("prob.")

	# Show the plot
	plt.show()

##---------------------------------
##  np.random.poisson()
##---------------------------------

# You just heard that the Poisson distribution is a limit of the Binomial distribution for rare events. This makes sense if you think about the stories. Say we do a Bernoulli trial every minute for an hour, each with a success probability of 0.1. We would do 60 trials, and the number of successes is Binomially distributed, and we would expect to get about 6 successes. This is just like the Poisson story we discussed in the video, where we get on average 6 hits on a website per hour. So, the Poisson distribution with arrival rate equal to np approximates a Binomial distribution for n Bernoulli trials with probability p of success (with n large and p small). Importantly, the Poisson distribution is often simpler to work with because it has only one parameter instead of two for the Binomial distribution.

# Let's explore these two distributions computationally. You will compute the mean and standard deviation of samples from a Poisson distribution with an arrival rate of 10. Then, you will compute the mean and standard deviation of samples from a Binomial distribution with parameters n and p such that np=10.
# You will see that for Binomial distribution with large n and small p, it approaches poisson dist

if False:
	# Draw 10,000 samples out of Poisson distribution: samples_poisson
	samples_poisson = np.random.poisson(10, 10000)

	# Print the mean and standard deviation
	print('Poisson:     ', np.mean(samples_poisson), np.std(samples_poisson))

	# Specify values of n and p to consider for Binomial: n, p
	n = [20, 100, 1000]
	p = [0.5, 0.1, 0.01]

	# Draw 10,000 samples for each n,p pair: samples_binomial
	for i in range(3):
		samples_binomial = np.random.binomial(n[i], p[i], 10000)
			
		# Print results
		print('n =', n[i], 'Binom:', np.mean(samples_binomial), np.std(samples_binomial))

# Was 2015 anomalous?
# 1990 and 2015 featured the most no-hitters of any season of baseball (there were seven). Given that there are on average 251/115 no-hitters per season, what is the probability of having seven or more in a season?
if False:
	# Draw 10,000 samples out of Poisson distribution: n_nohitters
	n_nohitters = np.random.poisson(float(251/115), 10000)

	# Compute number of samples that are seven or greater: n_large
	n_large = np.sum(n_nohitters>=7)

	# Compute probability of getting seven or more: p_large
	p_large = n_large/10000

	# Print the result
	print('Probability of seven or more no-hitters:', p_large)

# The result is about 0.007. This means that it is not that improbable to see a 7-or-more no-hitter season in a century. We have seen two in a century and a half, so it is not unreasonable.






