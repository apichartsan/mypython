import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Considering the problem of deciding if the pdf of two data sets are the same.
#	>> start  by concatenate two data samples
#	>> do permutation of the combined sample

# Set default Seaborn style
sns.set()

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

def permutation_sample(data1, data2):
	"""Generate a permutation sample from two data sets."""

	# Concatenate the data sets: data
	# Be sure to pass in data1 and data2 as one argument (data1, data2)
	data = np.concatenate((data1, data2))

	# Permute the concatenated array: permuted_data
	permuted_data = np.random.permutation(data)

	# Split the permuted array into two: perm_sample_1, perm_sample_2
	perm_sample_1 = permuted_data[:len(data1)]
	perm_sample_2 = permuted_data[len(data1):]

	return perm_sample_1, perm_sample_2

def draw_perm_reps(data_1, data_2, func, size=1):
	"""Generate multiple permutation replicates."""
	
	# Initialize array of replicates: perm_replicates
	perm_replicates = np.empty(size)
	
	for i in range(size):
		# Generate permutation sample
		perm_sample_1, perm_sample_2 = permutation_sample(data_1, data_2)
		
		# Compute the test statistic
		perm_replicates[i] = func(perm_sample_1, perm_sample_2)
	
	return perm_replicates

def diff_of_means(data_1, data_2):
	"""Difference in means of two arrays."""
	# The difference of means of data_1, data_2: diff
	diff = np.mean(data_1) - np.mean(data_2)
	
	return diff

##---------------------------------
## A/B test : The vote for the Civil Rights Act in 1964
##---------------------------------

# The Civil Rights Act of 1964 was one of the most important pieces of legislation ever passed in the USA. Excluding "present" and "abstain" votes, 153 House Democrats and 136 Republicans voted yea. However, 91 Democrats and 35 Republicans voted nay. Did party affiliation make a difference in the vote?

# To answer this question, you will evaluate the hypothesis that the party of a House member has no bearing on his or her vote. You will use the fraction of Democrats voting in favor as your test statistic and evaluate the probability of observing a fraction of Democrats voting in favor at least as small as the observed fraction of 153/244. (That's right, at least as small as. In 1964, it was the Democrats who were less progressive on civil rights issues.) To do this, permute the party labels of the House voters and then arbitrarily divide them into "Democrats" and "Republicans" and compute the fraction of Democrats voting yea.

# Construct arrays of data: dems, reps
dems = np.array([True] * 153 + [False] * 91)
reps = np.array([True] * 136 + [False] * 35)

def frac_yea_dems(dems, reps):
	"""Compute fraction of Democrat yea votes."""
	# Two inputs are required to use your draw_perm_reps() function, but the second is not used
	frac = np.sum(dems) / float(len(dems))
	return frac

# Acquire permutation samples: perm_replicates
perm_replicates = draw_perm_reps(dems, reps, frac_yea_dems, 10000)
print (np.mean(perm_replicates))
# Compute and print p-value: p
p = np.sum(perm_replicates <= 153/244) / float(len(perm_replicates))
print('p-value =', p)
# p-value = 0.0001

# This small p-value suggests that party identity had a lot to do with the voting. Importantly, the South had a higher fraction of Democrat representatives, and consequently also a more racist bias.



##---------------------------------
## A/B test : A time-on-website analog
##---------------------------------
print "A/B test : A time-on-website analog "
# It turns out that you already did a hypothesis test analogous to an A/B test where you are interested in how much time is spent on the website before and after an ad campaign. The frog tongue force (a continuous quantity like time on the website) is an analog. "Before" = Frog A and "after" = Frog B. Let's practice this again with something that actually is a before/after scenario.

# We return to the no-hitter data set. In 1920, Major League Baseball implemented important rule changes that ended the so-called "dead ball era". Importantly, the pitcher was no longer allowed to spit on or scuff the ball, an activity that greatly favors pitchers. In this problem you will perform an A/B test to determine if these rule changes resulted in a slower rate of no-hitters (i.e., longer average time between no-hitters) using the difference in mean inter-no-hitter time as your test statistic. The inter-no-hitter times for the respective eras are stored in the arrays nht_dead and nht_live, where "nht" is meant to stand for "no-hitter time."


nht_dead = np.array([  -1,  894,   10,  130,    1,  934,   29,    6,  485,  254,  372,
	   81,  191,  355,  180,  286,   47,  269,  361,  173,  246,  492,
	   462, 1319,   58,  297,   31, 2970,  640,  237,  434,  570,   77,
	   271,  563, 3365,   89,    0,  379,  221,  479,  367,  628,  843,
	   1613, 1101,  215,  684,  814,  278,  324,  161,  219,  545,  715,
	   966,  624,   29,  450,  107,   20,   91, 1325,  124, 1468,  104,
	   1309,  429,   62, 1878, 1104,  123,  251,   93,  188,  983,  166,
	   96,  702,   23,  524,   26,  299,   59,   39,   12,    2,  308,
	   1114,  813,  887])

nht_live = np.array([ 645, 2088,   42, 2090,   11,  886, 1665, 1084, 2900, 2432,  750,
	   4021, 1070, 1765, 1322,   26,  548, 1525,   77, 2181, 2752,  127,
	   2147,  211,   41, 1575,  151,  479,  697,  557, 2267,  542,  392,
	   73,  603,  233,  255,  528,  397, 1529, 1023, 1194,  462,  583,
	   37,  943,  996,  480, 1497,  717,  224,  219, 1531,  498,   44,
	   288,  267,  600,   52,  269, 1086,  386,  176, 2199,  216,   54,
	   675, 1243,  463,  650,  171,  327,  110,  774,  509,    8,  197,
	   136,   12, 1124,   64,  380,  811,  232,  192,  731,  715,  226,
	   605,  539, 1491,  323,  240,  179,  702,  156,   82, 1397,  354,
	   778,  603, 1001,  385,  986,  203,  149,  576,  445,  180, 1403,
	   252,  675, 1351, 2983, 1568,   45,  899, 3260, 1025,   31,  100,
	   2055, 4043,   79,  238, 3931, 2351,  595,  110,  215,    0,  563,
	   206,  660,  242,  577,  179,  157,  192,  192, 1848,  792, 1693,
	   55,  388,  225, 1134, 1172, 1555,   31, 1582, 1044,  378, 1687,
	   2915,  280,  765, 2819,  511, 1521,  745, 2491,  580, 2072, 6450,
	   578,  745, 1075, 1103, 1549, 1520,  138, 1202,  296,  277,  351,
	   391,  950,  459,   62, 1056, 1128,  139,  420,   87,   71,  814,
	   603, 1349,  162, 1027,  783,  326,  101,  876,  381,  905,  156,
	   419,  239,  119,  129,  467])

# Compute the observed difference in mean inter-no-hitter times: nht_diff_obs
nht_diff_obs = np.mean(nht_dead) - np.mean(nht_live)

# Acquire 10,000 permutation replicates of difference in mean no-hitter time: perm_replicates
perm_replicates = draw_perm_reps(nht_dead, nht_live, diff_of_means, 10000)


# Compute and print the p-value: p
p = np.sum(perm_replicates <= nht_diff_obs) / float(len(perm_replicates))
print('p-val =', p)
# p-val = 0.0001

# Your p-value is 0.0001, which means that only one out of your 10,000 replicates had a result as extreme as the actual difference between the dead ball and live ball eras. This suggests strong statistical significance. Watch out, though, you could very well have gotten zero replicates that were as extreme as the observed value. This just means that the p-value is quite small, almost certainly smaller than 0.001

# What should you have done first?
# That was a nice hypothesis test you just did to check out whether the rule changes in 1920 changed the rate of no-hitters. But what should you have done with the data first?
# Performed EDA, perhaps plotting the ECDFs of inter-no-hitter times in the dead ball and live ball eras.
# Always a good idea to do first! I encourage you to go ahead and plot the ECDFs right now. You will see by eye that the null hypothesis that the distributions are the same is almost certainly not true.


##---------------------------------
## Hypothesis test on Pearson correlation
##---------------------------------

# **********
# Simulating a null hypothesis concerning correlation
#The observed correlation between female illiteracy and fertility in the data set of 162 countries may just be by chance; the fertility of a given country may actually be totally independent of its illiteracy. You will test this null hypothesis in the next exercise.
#
#To do the test, you need to simulate the data assuming the null hypothesis is true. Of the following choices, which is the best way to to do it?

#Choose 162 random numbers to represent the illiteracy rate and 162 random numbers to represent the corresponding fertility rate.
#>> If you just randomly choose numbers, they have nothing at all to do with the measured data.
#
#Do a permutation test: Permute the illiteracy values but leave the fertility values fixed to generate a new set of (illiteracy, fertility) data.
#>> this exactly simulates the null hypothesis and does so more efficiently than the last option. It is exact because it uses all data and eliminates any correlation because which illiteracy value pairs to which fertility value is shuffled.
#
#Do a permutation test: Permute both the illiteracy and fertility values to generate a new set of (illiteracy, fertility data).
#>> This works perfectly, and is exact because it uses all data and eliminates any correlation because which illiteracy value pairs to which fertility value is shuffled. However, it is not necessary, and computationally inefficient, to permute both illiteracy and fertility..
# **********

#The observed correlation between female illiteracy and fertility may just be by chance; the fertility of a given country may actually be totally independent of its illiteracy. You will test this hypothesis. To do so, permute the illiteracy values but leave the fertility values fixed. This simulates the hypothesis that they are totally independent of each other. For each permutation, compute the Pearson correlation coefficient and assess how many of your permutation replicates have a Pearson correlation coefficient greater than the observed one.
#
#The function pearson_r() that you wrote in the prequel to this course for computing the Pearson correlation coefficient is already in your name space.

def pearson_r(x, y):
	"""Compute Pearson correlation coefficient between two arrays."""
	# Compute correlation matrix: corr_mat
	corr_mat = np.corrcoef(x, y)
	# Return entry [0,1]
	return corr_mat[0,1]

illiteracy = np.array([ 9.5, 49.2,  1. , 11.2,  9.8, 60. , 50.2, 51.2,  0.6,  1. ,  8.5,
					   6.1,  9.8,  1. , 42.2, 77.2, 18.7, 22.8,  8.5, 43.9,  1. ,  1. ,
					   1.5, 10.8, 11.9,  3.4,  0.4,  3.1,  6.6, 33.7, 40.4,  2.3, 17.2,
					   0.7, 36.1,  1. , 33.2, 55.9, 30.8, 87.4, 15.4, 54.6,  5.1,  1.1,
					   10.2, 19.8,  0. , 40.7, 57.2, 59.9,  3.1, 55.7, 22.8, 10.9, 34.7,
					   32.2, 43. ,  1.3,  1. ,  0.5, 78.4, 34.2, 84.9, 29.1, 31.3, 18.3,
					   81.8, 39. , 11.2, 67. ,  4.1,  0.2, 78.1,  1. ,  7.1,  1. , 29. ,
					   1.1, 11.7, 73.6, 33.9, 14. ,  0.3,  1. ,  0.8, 71.9, 40.1,  1. ,
					   2.1,  3.8, 16.5,  4.1,  0.5, 44.4, 46.3, 18.7,  6.5, 36.8, 18.6,
					   11.1, 22.1, 71.1,  1. ,  0. ,  0.9,  0.7, 45.5,  8.4,  0. ,  3.8,
					   8.5,  2. ,  1. , 58.9,  0.3,  1. , 14. , 47. ,  4.1,  2.2,  7.2,
					   0.3,  1.5, 50.5,  1.3,  0.6, 19.1,  6.9,  9.2,  2.2,  0.2, 12.3,
					   4.9,  4.6,  0.3, 16.5, 65.7, 63.5, 16.8,  0.2,  1.8,  9.6, 15.2,
					   14.4,  3.3, 10.6, 61.3, 10.9, 32.2,  9.3, 11.6, 20.7,  6.5,  6.7,
					   3.5,  1. ,  1.6, 20.5,  1.5, 16.7,  2. ,  0.9])

fertility = np.array([1.769, 2.682, 2.077, 2.132, 1.827, 3.872, 2.288, 5.173, 1.393,
					  1.262, 2.156, 3.026, 2.033, 1.324, 2.816, 5.211, 2.1  , 1.781,
					  1.822, 5.908, 1.881, 1.852, 1.39 , 2.281, 2.505, 1.224, 1.361,
					  1.468, 2.404, 5.52 , 4.058, 2.223, 4.859, 1.267, 2.342, 1.579,
					  6.254, 2.334, 3.961, 6.505, 2.53 , 2.823, 2.498, 2.248, 2.508,
					  3.04 , 1.854, 4.22 , 5.1  , 4.967, 1.325, 4.514, 3.173, 2.308,
					  4.62 , 4.541, 5.637, 1.926, 1.747, 2.294, 5.841, 5.455, 7.069,
					  2.859, 4.018, 2.513, 5.405, 5.737, 3.363, 4.89 , 1.385, 1.505,
					  6.081, 1.784, 1.378, 1.45 , 1.841, 1.37 , 2.612, 5.329, 5.33 ,
					  3.371, 1.281, 1.871, 2.153, 5.378, 4.45 , 1.46 , 1.436, 1.612,
					  3.19 , 2.752, 3.35 , 4.01 , 4.166, 2.642, 2.977, 3.415, 2.295,
					  3.019, 2.683, 5.165, 1.849, 1.836, 2.518, 2.43 , 4.528, 1.263,
					  1.885, 1.943, 1.899, 1.442, 1.953, 4.697, 1.582, 2.025, 1.841,
					  5.011, 1.212, 1.502, 2.516, 1.367, 2.089, 4.388, 1.854, 1.748,
					  2.978, 2.152, 2.362, 1.988, 1.426, 3.29 , 3.264, 1.436, 1.393,
					  2.822, 4.969, 5.659, 3.24 , 1.693, 1.647, 2.36 , 1.792, 3.45 ,
					  1.516, 2.233, 2.563, 5.283, 3.885, 0.966, 2.373, 2.663, 1.251,
					  2.052, 3.371, 2.093, 2.   , 3.883, 3.852, 3.718, 1.732, 3.928])

print " Hypothesis test on Pearson correlation "
# Compute observed correlation: r_obs
r_obs = pearson_r(illiteracy, fertility)

# Initialize permutation replicates: perm_replicates
perm_replicates = np.empty(10000)

# Draw replicates
for i in range(len(perm_replicates)):
	# Permute illiteracy measurments: illiteracy_permuted
	illiteracy_permuted = np.random.permutation(illiteracy)

	# Compute Pearson correlation
	perm_replicates[i] = pearson_r(illiteracy_permuted, fertility)

# Compute p-value: p
p = np.sum(perm_replicates >= r_obs) / float(len(perm_replicates))
print('p-val =', p)
# p-val = 0.0
# You got a p-value of zero. In hacker statistics, this means that your p-value is very low, since you never got a single replicate in the 10,000 you took that had a Pearson correlation greater than the observed one. You could try increasing the number of replicates you take to continue to move the upper bound on your p-value lower and lower.



##---------------------------------
## Hypothesis test: Do neonicotinoid insecticides have unintended consequences?
## Bootstrap hypothesis test on bee sperm counts
##---------------------------------
print " Hypothesis test on bee sperm counts "

# As a final exercise in hypothesis testing before we put everything together in our case study in the next chapter, you will investigate the effects of neonicotinoid insecticides on bee reproduction. These insecticides are very widely used in the United States to combat aphids and other pests that damage plants.
# In a recent study, Straub, et al. (Proc. Roy. Soc. B, 2016) investigated the effects of neonicotinoids on the sperm of pollinating bees. In this and the next exercise, you will study how the pesticide treatment affected the count of live sperm per half milliliter of semen.
# First, we will do EDA, as usual. Plot ECDFs of the alive sperm count for untreated bees (stored in the Numpy array control) and bees treated with pesticide (stored in the Numpy array treated).

control = np.array([ 4.159234,  4.408002,  0.172812,  3.498278,  3.104912,  5.164174,
	   6.615262,  4.633066,  0.170408,  2.65    ,  0.0875  ,  1.997148,
	   6.92668 ,  4.574932,  3.896466,  5.209814,  3.70625 ,  0.      ,
	   4.62545 ,  3.01444 ,  0.732652,  0.4     ,  6.518382,  5.225   ,
	   6.218742,  6.840358,  1.211308,  0.368252,  3.59937 ,  4.212158,
	   6.052364,  2.115532,  6.60413 ,  5.26074 ,  6.05695 ,  6.481172,
	   3.171522,  3.057228,  0.218808,  5.215112,  4.465168,  2.28909 ,
	   3.732572,  2.17087 ,  1.834326,  6.074862,  5.841978,  8.524892,
	   4.698492,  2.965624,  2.324206,  3.409412,  4.830726,  0.1     ,
	   0.      ,  4.101432,  3.478162,  1.009688,  4.999296,  4.32196 ,
	   0.299592,  3.606032,  7.54026 ,  4.284024,  0.057494,  6.036668,
	   2.924084,  4.150144,  1.256926,  4.666502,  4.806594,  2.52478 ,
	   2.027654,  2.52283 ,  4.735598,  2.033236,  0.      ,  6.177294,
	   2.601834,  3.544408,  3.6045  ,  5.520346,  4.80698 ,  3.002478,
	   3.559816,  7.075844, 10.      ,  0.139772,  6.17171 ,  3.201232,
	   8.459546,  0.17857 ,  7.088276,  5.496662,  5.415086,  1.932282,
	   3.02838 ,  7.47996 ,  1.86259 ,  7.838498,  2.242718,  3.292958,
	   6.363644,  4.386898,  8.47533 ,  4.156304,  1.463956,  4.533628,
	   5.573922,  1.29454 ,  7.547504,  3.92466 ,  5.820258,  4.118522,
	   4.125   ,  2.286698,  0.591882,  1.273124,  0.      ,  0.      ,
	   0.      , 12.22502 ,  7.601604,  5.56798 ,  1.679914,  8.77096 ,
	   5.823942,  0.258374,  0.      ,  5.899236,  5.486354,  2.053148,
	   3.25541 ,  2.72564 ,  3.364066,  2.43427 ,  5.282548,  3.963666,
	   0.24851 ,  0.347916,  4.046862,  5.461436,  4.066104,  0.      ,
	   0.065   ])

treated = np.array([1.342686, 1.058476, 3.793784, 0.40428 , 4.528388, 2.142966,
	   3.937742, 0.1375  , 6.919164, 0.      , 3.597812, 5.196538,
	   2.78955 , 2.3229  , 1.090636, 5.323916, 1.021618, 0.931836,
	   2.78    , 0.412202, 1.180934, 2.8674  , 0.      , 0.064354,
	   3.008348, 0.876634, 0.      , 4.971712, 7.280658, 4.79732 ,
	   2.084956, 3.251514, 1.9405  , 1.566192, 0.58894 , 5.219658,
	   0.977976, 3.124584, 1.297564, 1.433328, 4.24337 , 0.880964,
	   2.376566, 3.763658, 1.918426, 3.74    , 3.841726, 4.69964 ,
	   4.386876, 0.      , 1.127432, 1.845452, 0.690314, 4.185602,
	   2.284732, 7.237594, 2.185148, 2.799124, 3.43218 , 0.63354 ,
	   1.142496, 0.586   , 2.372858, 1.80032 , 3.329306, 4.028804,
	   3.474156, 7.508752, 2.032824, 1.336556, 1.906496, 1.396046,
	   2.488104, 4.759114, 1.07853 , 3.19927 , 3.814252, 4.275962,
	   2.817056, 0.552198, 3.27194 , 5.11525 , 2.064628, 0.      ,
	   3.34101 , 6.177322, 0.      , 3.66415 , 2.352582, 1.531696])

# Compute x,y values for ECDFs
x_control, y_control = ecdf(control)
x_treated, y_treated = ecdf(treated)

# Plot the ECDFs
plt.plot(x_control, y_control, marker='.', linestyle='none')
plt.plot(x_treated, y_treated, marker='.', linestyle='none')

# Set the margins
plt.margins(0.02)

# Add a legend
plt.legend(('control', 'treated'), loc='lower right')

# Label axes and show plot
plt.xlabel('millions of alive sperm per mL')
plt.ylabel('ECDF')
plt.show()
# The ECDFs show a pretty clear difference between the treatment and control; treated bees have fewer alive sperm. Let's now do a hypothesis test in the next exercise.

# Now, you will test the following hypothesis: On average, male bees treated with neonicotinoid insecticide have the same number of active sperm per milliliter of semen than do untreated male bees. You will use the difference of means as your test statistic.

# Notice that this is to test the "Mean", not the distribution. >> Bootstrap

# Compute the difference in mean sperm count: diff_means
diff_means = np.mean(control) - np.mean(treated)

# Compute mean of pooled data: mean_count
mean_count = np.mean(np.concatenate((control, treated)))

# Generate shifted data sets
control_shifted = control - np.mean(control) + mean_count
treated_shifted = treated - np.mean(treated) + mean_count

# Generate bootstrap replicates
bs_reps_control = draw_bs_reps(control_shifted,
							   np.mean, size=10000)
bs_reps_treated = draw_bs_reps(treated_shifted,
							   np.mean, size=10000)

# Get replicates of difference of means: bs_replicates
bs_replicates = bs_reps_control - bs_reps_treated

# Compute and print p-value: p
p = np.sum(bs_replicates >= diff_means) / float(len(bs_replicates))
print('p-value =', p)

# The p-value is small, most likely less than 0.0001, since you never saw a bootstrap replicated with a difference of means at least as extreme as what was observed. In fact, when I did the calculation with 10 million replicates, I got a p-value of 2e-05















