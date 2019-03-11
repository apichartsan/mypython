
'''
    I found that there is problem when using, e.g., df_coppy["Age"].hist()
		>> this might be related to old version of matplotlib
		
	So, I try updating matplotlib
		$ sudo pip install --upgrade matplotlib
			>> Found existing installation: matplotlib 1.1.1
			
	Make sure you have the most up-to-date version of pip installed, by running
		$ pip install --upgrade pip
	
	Let's remove old matplotlib
		$ cd /System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python/
		$ sudo rm -r matplotlib
		$ sudo rm matplotlib-1.1.1-py2.7.egg-info
		$ sudo pip install matplotlib

'''


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('titanic_data.csv')

#df_coppy = df.copy()
#df_coppy[df_coppy['Embarked'].isnull()]
#df_coppy.isnull().sum()

#df_coppy.dropna(inplace=True)
#df_coppy.shape

df_coppy = df.copy()
df_coppy.isnull().sum()
df_coppy.dropna(subset=['Embarked'],inplace=True)
df_coppy.shape
df_coppy.isnull().sum()
df_coppy['Age'].isnull().sum()

mean = df['Age'].mean()
df_coppy['Age'].fillna(mean).isnull().sum()
df_coppy['Age'].fillna(mean,inplace=True)
df_coppy.isnull().sum()


#df = pd.read_csv('titanic_data.csv') # df ==> data frame
#df_coppy = df.copy()
#
#df_coppy["Age"]
#df_coppy["Age"].mean()
#df_coppy["Age"].hist()
#plt.show()
#plt.show(block = False) # this is to keep figure display and not blocking typing command

## the workflow below is better
f1 = plt.figure(1)
f2 = plt.figure(2)

df_coppy['Age'].hist(figure=f1)
f1.show()
df_coppy['Fare'].hist(figure=f2)
f2.show()


# add a new column for nunerical values assigned for Sex
df_coppy.loc[(df_coppy['Sex']=='female'), 'Sex_num'] = 1
df_coppy.loc[(df_coppy['Sex']=='male'), 'Sex_num'] = 0


## visualization using plt
f1 = plt.figure(1)
plt.hist(df_coppy['Age'].dropna(),figure=f1)
f1.show()


'''
	Now, we want to use library 'seaborn' for plotting
	The video says using the follwing
	$ pip install seaborn
		>> error: invalid command 'bdist_wheel'
		>> Failed building wheel for seaborn
		>> Installing collected packages: scipy, seaborn
			 >> Found existing installation: scipy 0.11.0


	Make sure you have the most up-to-date version of pip installed, by running
	$ sudo pip install --upgrade pip
	
	Let's remove old scipy
	$ sudo rm -r scipy
	$ sudo rm scipy-0.11.0-py2.7.egg-info
	$ cd -
	$ sudo pip install seaborn

'''

import seaborn as sns

f1 = plt.figure(1)
sns.distplot(df_coppy['Age'].dropna())
f2 = plt.figure(2)
sns.distplot( df_coppy[df_coppy['Age']>30]['Age'].dropna())



'''
	lets install scikit-learn :
	 >> from any dir type
	 
	$ sudo pip install scikit-learn
		>> Successfully installed scikit-learn-0.20.2
		
'''



