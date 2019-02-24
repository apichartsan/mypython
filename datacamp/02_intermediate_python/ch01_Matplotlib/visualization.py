
import matplotlib.pyplot as plt

##----  Line plot and scatter plot

year = [1950, 1970, 1990, 2010]
pop = [2.519, 3.692, 5.263, 6.972]
plt.plot(year, pop)
plt.show() # display all figures and block until the figures have been closed

plt.scatter(year, pop)
#plt.show(block=False) # use this to un-block the figures (but cannot update that figures ?)

# Put the x-axis on a logarithmic scale
plt.xscale('log')
plt.show()

values = [1,2,3,2,3,4,4,4,5,5,6,6,7]
plt.hist(values,4)

# Strings
xlab = 'GDP per Capita [in USD]'
ylab = 'Life Expectancy [in years]'
title = 'World Development in 2007'

# Add axis labels
plt.xlabel(xlab)
plt.ylabel(ylab)

# Add title
plt.title(title)

# Definition of tick_val and tick_lab
tick_val = [1000, 10000, 100000]
tick_lab = ['1k', '10k', '100k']

# Adapt the ticks on the x-axis
plt.xticks(tick_val,tick_lab)

# Update: set s argument to np_pop, the size of the dots
plt.scatter(gdp_cap, life_exp, s = np_pop)

# Specify c and alpha inside plt.scatter() (color and opacity)
plt.scatter(x = gdp_cap, y = life_exp, s = np.array(pop) * 2, c = col, alpha = 0.8)

# Add grid() call
plt.grid(True)

# Additional customizations
plt.text(1550, 71, 'India')
plt.text(5700, 80, 'China')
