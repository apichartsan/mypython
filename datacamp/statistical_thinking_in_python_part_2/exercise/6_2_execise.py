import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd


# Consider something that might look similar to 6_1 at first but it actually not

# We have sample X (500 observations) with mean of 0 and std of 3 and sample Y (200 observations) with mean of 0 and std of 4

# Combine these two samples and find the mean and std of the combined sample.

# The formular for the mean and std of the combined sample can be found here
# https://www.emathzone.com/tutorials/basic-statistics/combined-variance.html
# The formula for std can also be written as
#
# sigma_z^2 = {(nx*sigma_x^2)+(ny*sigma_y^2)+(nx*x_bar^2)+(ny*y_bar^2)/(nx+ny)} - z_bar^2
#
nx = 500
ny = 200
x_bar = 0
y_bar = 0
sigma_x = 3
sigma_y = 4
#nx = 50
#ny = 40
#x_bar = 63
#y_bar = 54
#sigma_x = 9
#sigma_y = 6

z_bar = ((nx*x_bar)+(ny*y_bar))/float(nx+ny)
sigma_z_2 = ((nx*(sigma_x**2))+(ny*(sigma_y**2))+(nx*(x_bar**2))+(ny*(y_bar**2)))/float(nx+ny) - (z_bar**2)
sigma_z = np.sqrt(sigma_z_2)
print ' -------------------- '
print ' z_bar   ; ', z_bar
print ' sigma_z ; ', sigma_z, '\n'

# z_bar   ;  0.0
# sigma_z ;  3.3166247903554



# if we want to do hacker stat, there is a subtlety because we can only assume the true parameter sigma and draw sample of 500 and 200 obs from the poppulation
# So the above should be the correct way to do.
# But I include the hacker stat way here.

samples_x = np.random.normal(0, 3, size=500) # note that here we take the obs std as a parameter sigma
samples_y = np.random.normal(0, 4, size=200)

samples_z = np.concatenate((samples_x,samples_y))
_ = plt.hist(samples_z)
plt.show()

prob  = (np.sum(samples_z > 5) / float(len(samples_z)))

print ' mean, std of x : ', np.mean(samples_x), np.std(samples_x)
print ' mean, std of y : ', np.mean(samples_y), np.std(samples_y)
print ' mean, std of z : ', np.mean(samples_z), np.std(samples_z)
print ' total n : ', len(samples_z)

# mean, std of x :  0.042434649996137934 2.9370649321320634
# mean, std of y :  -0.3148564468515304 4.187934290684451
# mean, std of z :  -0.05964852053176727 3.3464630873253753
# total n :  700



# Below are the results of 6_1
# mean, std of x :  -0.011161342683833422 0.9923427861884138
# mean, std of y :  0.00019590157158203922 1.0014151148010033
# mean, std of z :  -0.0327004217651721 4.983066010099489
# total n :  10000




