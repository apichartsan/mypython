import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
#import ROOT
from ROOT import *
import array as arr

# Create bee swarm plot with Seaborn's default settings
sns.set()

belmont_no_outliers = np.array([148.51, 146.65, 148.52, 150.7 , 150.42, 150.88, 151.57, 147.54,
	   149.65, 148.74, 147.86, 148.75, 147.5 , 148.26, 149.71, 146.56,
	   151.19, 147.88, 149.16, 148.82, 148.96, 152.02, 146.82, 149.97,
	   146.13, 148.1 , 147.2 , 146.  , 146.4 , 148.2 , 149.8 , 147.  ,
	   147.2 , 147.8 , 148.2 , 149.  , 149.8 , 148.6 , 146.8 , 149.6 ,
	   149.  , 148.2 , 149.2 , 148.  , 150.4 , 148.8 , 147.2 , 148.8 ,
	   149.6 , 148.4 , 148.4 , 150.2 , 148.8 , 149.2 , 149.2 , 148.4 ,
	   150.2 , 146.6 , 149.8 , 149.  , 150.8 , 148.6 , 150.2 , 149.  ,
	   148.6 , 150.2 , 148.2 , 149.4 , 150.8 , 150.2 , 152.2 , 148.2 ,
	   149.2 , 151.  , 149.6 , 149.6 , 149.4 , 148.6 , 150.  , 150.6 ,
	   149.2 , 152.6 , 152.8 , 149.6 , 151.6 , 152.8 , 153.2 , 152.4 ,
	   152.2 ])


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


##---------------------------------
##  Normal distribution np.random.normal()
##---------------------------------

# In this exercise, you will explore the Normal PDF and also learn a way to plot a PDF of a known distribution using hacker statistics. Specifically, you will plot a Normal PDF for various values of the variance.
if False:
	# Draw 100000 samples from Normal distribution with stds of interest: samples_std1, samples_std3, samples_std10
	samples_std1 = np.random.normal(20, 1, size=100000)
	samples_std3 = np.random.normal(20, 3, size=100000)
	samples_std10 = np.random.normal(20, 10, size=100000)

	# Make histograms
	_ = plt.hist(samples_std1, bins=100, normed=True, histtype='step')
	_ = plt.hist(samples_std3, bins=100, normed=True, histtype='step')
	_ = plt.hist(samples_std10, bins=100, normed=True, histtype='step')

	# Make a legend, set limits and show plot
	_ = plt.legend(('std = 1', 'std = 3', 'std = 10'))
	plt.ylim(-0.01, 0.42)
	plt.show()

	# Now that you have a feel for how the Normal PDF looks, let's consider its CDF. Using the samples you generated in the last exercise (in your namespace as samples_std1, samples_std3, and samples_std10), generate and plot the CDFs.

	# Generate CDFs
	x_std1, y_std1 = ecdf(samples_std1)
	x_std3, y_std3 = ecdf(samples_std3)
	x_std10, y_std10 = ecdf(samples_std10)

	# Plot CDFs
	_ = plt.plot(x_std1, y_std1, marker = '.', linestyle = 'none')
	_ = plt.plot(x_std3, y_std3, marker = '.', linestyle = 'none')
	_ = plt.plot(x_std10, y_std10, marker = '.', linestyle = 'none')

	# Make a legend and show the plot
	_ = plt.legend(('std = 1', 'std = 3', 'std = 10'), loc='lower right')
	plt.show()

# Are the Belmont Stakes results Normally distributed?
# Since 1926, the Belmont Stakes is a 1.5 mile-long race of 3-year old thoroughbred horses. Secretariat ran the fastest Belmont Stakes in history in 1973. While that was the fastest year, 1970 was the slowest because of unusually wet and sloppy conditions. With these two outliers removed from the data set, compute the mean and standard deviation of the Belmont winners' times. Sample out of a Normal distribution with this mean and standard deviation using the np.random.normal() function and plot a CDF. Overlay the ECDF from the winning Belmont times. Are these close to Normally distributed?
if False:
	# Compute mean and standard deviation: mu, sigma
	mu = np.mean(belmont_no_outliers)
	sigma = np.std(belmont_no_outliers)

	# Sample out of a normal distribution with this mu and sigma: samples
	samples = np.random.normal(mu, sigma, 10000)

	# Get the CDF of the samples and of the data
	x_theor, y_theor = ecdf(samples)
	x, y = ecdf(belmont_no_outliers)

	# Plot the CDFs and show the plot
	_ = plt.plot(x_theor, y_theor)
	_ = plt.plot(x, y, marker='.', linestyle='none')
	_ = plt.xlabel('Belmont winning time (sec.)')
	_ = plt.ylabel('CDF')
	plt.show()

	# The theoretical CDF and the ECDF of the data suggest that the winning Belmont times are, indeed, Normally distributed. This also suggests that in the last 100 years or so, there have not been major technological or training advances that have significantly affected the speed at which horses can run this race.


	# What are the chances of a horse matching or beating Secretariat's record?
	# Assume that the Belmont winners' times are Normally distributed (with the 1970 and 1973 years removed), what is the probability that the winner of a given Belmont Stakes will run it as fast or faster than Secretariat (of 144 seconds)?
	# Take a million samples out of the Normal distribution: samples
	samples = np.random.normal(mu, sigma, 1000000)

	# Compute the fraction that are faster than 144 seconds: prob
	prob =  np.sum(samples<=144)/len(samples)

	# Print the result
	print('Probability of besting Secretariat:', prob)

	# Great work! We had to take a million samples because the probability of a fast time is very low and we had to be sure to sample enough. We get that there is only a 0.06% chance of a horse running the Belmont as fast as Secretariat.



##---------------------------------
##  Exponential distribution np.random.exponential()
##---------------------------------
# How might we expect the time between Major League no-hitters to be distributed? Be careful here: a few exercises ago, we considered the probability distribution for the number of no-hitters in a season. Now, we are looking at the probability distribution of the time between no hitters.
# Ans: exponentially distributed
# ex2: The number of bus arrive in an hour is Poison distributed. The time between arrival is exponentially distributed.
# The Exponential distribution describes the waiting times between rare events,



# If you have a story, you can simulate it!
#
#Sometimes, the story describing our probability distribution does not have a named distribution to go along with it. In these cases, fear not! You can always simulate it. We'll do that in this and the next exercise.
#In earlier exercises, we looked at the rare event of no-hitters in Major League Baseball. Hitting the cycle is another rare baseball event. When a batter hits the cycle, he gets all four kinds of hits, a single, double, triple, and home run, in a single game. Like no-hitters, this can be modeled as a Poisson process, so the time between hits of the cycle are also Exponentially distributed.
#How long must we wait to see both a no-hitter and then a batter hit the cycle? The idea is that we have to wait some time for the no-hitter, and then after the no-hitter, we have to wait for hitting the cycle. Stated another way, what is the total waiting time for the arrival of two different Poisson processes? The total waiting time is the time waited for the no-hitter, plus the time waited for the hitting the cycle.
#Now, you will write a function to sample out of the distribution described by this story.


def successive_poisson(tau1, tau2, size=1):
	"""Compute time for arrival of 2 successive Poisson processes."""
		# Draw samples out of first exponential distribution: t1
		t1 = np.random.exponential(tau1, size=size)
			
			# Draw samples out of second exponential distribution: t2
			t2 = np.random.exponential(tau2, size=size)
				
    return t1 + t2


if False:
	# Now, you'll use your sampling function to compute the waiting time to observe a no-hitter and hitting of the cycle. The mean waiting time for a no-hitter is 764 games, and the mean waiting time for hitting the cycle is 715 games.

	# Draw samples of waiting times: waiting_times
	waiting_times = successive_poisson(764,715,100000)

	# Make the histogram
	_ = plt.hist(waiting_times, bins=100, normed=True, histtype='step')

	# Label axes
	plt.xlabel("waiting times for observing a no-hitter and a hitting of the cycle")

	# Show the plot
	plt.show()

	# Notice that the PDF is peaked, unlike the waiting time for a single Poisson process. For fun (and enlightenment), I encourage you to also plot the CDF.
