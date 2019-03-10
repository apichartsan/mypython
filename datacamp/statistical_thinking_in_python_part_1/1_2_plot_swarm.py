import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

df = pd.read_csv('iris.csv')
df.head() #  This will let you identify which column names


# Create bee swarm plot with Seaborn's default settings
sns.set()
sns.swarmplot(x='species', y='petal_length', data=df)
# Label the axes
plt.xlabel('species')
plt.ylabel('petal length (cm)')
# Show the plot
plt.show()

# histograms suffers from the variant in binning, this could casue misinterpretation of data
# swarm plots show all data, so no binning effect. But when there are a lot of data points swarm plots are not good choice.