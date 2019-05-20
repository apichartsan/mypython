import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd


# sample X and Y are normally distributed with mean = 0 and std = 1. Sample Z is distributed as 3X +4Y. What is the probability that an element in sample Z has value > 5?

# ** Note that here we are not being asked about combined samples, so this is not to concatinate the two samples !

samples_x = np.random.normal(0, 1, size=10000)
samples_y = np.random.normal(0, 1, size=10000)

samples_z = 3*samples_x + 4*samples_y
_ = plt.hist(samples_z)
plt.show()

prob  = (np.sum(samples_z > 5) / float(len(samples_z)))

print ' mean, std of x : ', np.mean(samples_x), np.std(samples_x)
print ' mean, std of y : ', np.mean(samples_y), np.std(samples_y)
print ' mean, std of z : ', np.mean(samples_z), np.std(samples_z)
print ' total n : ', len(samples_z)
print ' n > 5   : ', np.sum(samples_z > 5)
print ' prob    : ', prob

# mean, std of x :  -0.011161342683833422 0.9923427861884138
# mean, std of y :  0.00019590157158203922 1.0014151148010033
# mean, std of z :  -0.0327004217651721 4.983066010099489
# total n :  10000
# n > 5   :  1539
# prob    :  0.1539



# Note: >> std_z  = 4.98  which is ~ sqrt(3^2 + 4^2) = 5

# (1) you have to know that suppose X is a random variable which follows standard normal distribution mu_x and stdx
#     Then, multiply every element by a constant c give normal distribution with mu = c*mu_X and std = c * stdx
#     BOTH 'mean' and 'std' shift linearly !
#     i.e.
#	  X -> N(mu_x, sigma_x^2)
#	  Z -> c * X
#	  Then  Z -> N( c*mu_x, c^2*sigma_x^2)
# This can be easily proof by using the property sigma_x^2 = <x^2> - <x>^2

# (2) Then, we can think of the problem as adding 2 gaussian function mu_x = 0 and stdx = 3, mu_y = 0 and stdy = 4
# X -> N(mu_x, sigma_x^2)
# Y -> N(mu_y, sigma_y^2)
# Z -> X + Y
# Then  Z -> N( mu_x + mu_y, sigma_x^2 + sigma_y^2 )
# Proof can be found here : https://en.wikipedia.org/wiki/Sum_of_normally_distributed_random_variables

# Using (1) and (2) ;
#	>> mean is 0
#	>> std  = sqrt(3^2 + 4^2) = 5
# so, the above question is essentially asking p > 1sigma which is (100%-68%)/2 = 16%
# You can answer this question without using hacker stats !













