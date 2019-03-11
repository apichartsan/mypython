
'''
    # dataset at : https://www.kaggle.com/prkukunoor/TitanicDataset
        >> I sign up the account using email particlebaby1984@gmail.com
            >> username: apichartsan
            >> sign in with facebook particlebaby1984@gmail.com
            
    You get a .zip file titanicdataset.zip.
    You can unzip it by
    >> unzip titanicdataset.zip
    Now you have the .csv file : titanic_data.csv
'''

'''
    $ type -a python
    My python 2.7 is at /System/Library/Frameworks/Python.framework/Versions/2.7/bin
    My 3rd party library dir is at ? /Library/Python/2.7/site-packages
        >> you can see that I already have the 'swampy' library which I did intalled it
                when I studied 'ThinkPython'

'''

'''
 First, I would like to learn how to install python module/library.
    >> I will use pip to get libralies.
    >> But pip has not been installed in mac OSX by default
    
 (1) Get the 'Python pip'. 
        This video is super useful:
            >> https://www.youtube.com/watch?v=yBdZZGPpYxg
        https://bootstrap.pypa.io/get-pip.py
    On your terminal:
    $ cd /Users/apichart/Documents/01_Python_Lecture/Algo_Addict/02_Python_DataSc_beginners
    $ curl https://bootstrap.pypa.io/get-pip.py >> get-pip.py
    $ sudo python get-pip.py

    Now you can see the 'pip' and 'wheel' in /Library/Python/2.7/site-packages

    Test by run
    $ pip

 (2) https://www.youtube.com/watch?v=FKwicZF7xNE
    So, I want these libraries: pandas,numpy,matplotlib

    $ sudo pip install matplotlib
        >> note that 'numpy' is dependency of matplotlib, the above command should get 'numpy' too
        >> But when I do this I got
            >> 'Requirement already satisfied: matplotlib in /System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python (1.1.1)'
            >> which means I already have matplotlib installed
            >> Try it by import it in python shell
            
    $ sudo pip install pandas
        >> it tried to install numpy but failed
        >> 'Collecting numpy>=1.9.0 (from pandas)'
        >> 'Found existing installation: numpy 1.6.2
                Cannot uninstall 'numpy'.
                It is a distutils installed project and thus we cannot
                accurately determine which files belong to it which
                would lead to only a partial uninstall.'

       >> let's remove old numpy (I installed it when I study ThinkPython) first:
    $ cd /System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python/
    $ sudo rm -r numpy
    $ sudo rm numpy-1.6.2-py2.7.egg-info
    $ cd -
    $ sudo pip uninstall numpy
    $ sudo pip install pandas
 

    OK. I think we are good to go. !!!

'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('titanic_data.csv') # df ==> data frame

###print df
##print df.head()
##print df.tail()
##
###print df.dtypes
###print len(df)
###print df.shape
###print df.info()
###print df.describe()

##print df.loc[0]
##print df.loc[10]
##print df.iloc[-1]
##print df.iloc[-10]

##print df.Age
##print df['Age']
##print type(df.Age)

##print df['Age'] == 35
##print type(df['Age'] == 35)
##
##print df[df['Age'] == 35]
##print len(df[df['Age'] == 35])

##print df[df['Sex'] == 'female']

#print df[df['Survived'] == 1]

##print df['Survived'].value_counts()
##print df['Survived'].value_counts().sum()

##sur = df['Survived'].value_counts()[1]
##psum = df['Survived'].value_counts().sum()
##print '% of sur', sur, psum, float(float(sur)/psum)

##menSur = df[df['Sex'] == 'male']['Survived'].value_counts()[1]
##sumMen = df[df['Sex'] == 'male']['Survived'].value_counts().sum()
##print '% of men that sur', menSur, sumMen, float(float(menSur)/sumMen)
##
##fmenSur = df[df['Sex'] == 'female']['Survived'].value_counts()[1]
##sumfMen = df[df['Sex'] == 'female']['Survived'].value_counts().sum()
##print '% of fmen that sur', fmenSur, sumfMen, float(float(fmenSur)/sumfMen)

## Exercise
#c1Test = df['Pclass'].value_counts()[1] # note that what in [] is refer with the value, not the index
#c2Test = df['Pclass'].value_counts()[2]
#c3Test = df['Pclass'].value_counts()[3]
#
#sumPclass = df['Pclass'].value_counts().sum()
#c1 = len(df[df['Pclass'] == 1])
#c2 = len(df[df['Pclass'] == 2])
#c3 = len(df[df['Pclass'] == 3])
#
#print sumPclass, c1Test, c2Test, c3Test
#print sumPclass, c1, c2, c3, c1+c2+c3
#print '% of pClass '
#print '  c1 ', float(c1)/sumPclass
#print '  c2 ', float(c2)/sumPclass
#print '  c3 ', float(c3)/sumPclass
#
#
#### This is tricky
###c1Cond = df['Pclass'] == 1 # this has 891 row of bool
###df['Pclass'] == 1 # this has 891 row of bool
###df[df['Pclass'] == 1] # df has 891 row of data and can use c1Cond as a 'conditional'
###df[c1Cond]  # df has 891 row of data and can use c1Cond as a 'conditional'
###
###df[df['Pclass'] == 1] # now, this has 216 row
###df[df['Pclass'] == 1]['Survived'] == 1] # this has 216 row of bool
###df[df[df['Pclass'] == 1]['Survived'] == 1]] # is not possible since df[] has 891 row
###df[df['Pclass'] == 1][df[df['Pclass'] == 1]['Survived'] == 1] # this is ok
#
## This might look more transparent
#c1Cond = df['Pclass'] == 1 # condition of c1, this has 891 rows of bool
#dfWithc1 = df[c1Cond] # df has 891 rows of data and can use c1Cond as a 'conditional', now dfWithc1 has 216 rows 
#c1SurCond = dfWithc1['Survived'] == 1 # condition of c1Sur, this has 216 rows of bool
#dfWithc1Sur = dfWithc1[c1SurCond] # dfWithc1 has 216 rows of data and can use c1SurCond as a 'conditional'
#surC1 = len(dfWithc1Sur)
#
## I can just use .value_counts() :
##print dfWithc1['Survived'].value_counts()
#print "surC1", surC1, dfWithc1['Survived'].value_counts()[1] # note that what in [] is refer with the value, not the index
#
#c2Cond = df['Pclass'] == 2 
#dfWithc2 = df[c2Cond] 
#c2SurCond = dfWithc2['Survived'] == 1 
#dfWithc2Sur = dfWithc2[c2SurCond] 
#surC2 = len(dfWithc2Sur)
#
#c3Cond = df['Pclass'] == 3 
#dfWithc3 = df[c3Cond] 
#c3SurCond = dfWithc3['Survived'] == 1 
#dfWithc3Sur = dfWithc3[c3SurCond] 
#surC3 = len(dfWithc3Sur)
#
#print '% of survival '
#print '  c1 ', surC1/float(c1)
#print '  c2 ', surC2/float(c2)
#print '  c3 ', surC3/float(c3)


# add Rows
df_coppy = df.copy()
df_coppy.tail()
df_coppy.loc[891] = [892,0,3,'AAAA','male',32.0,0,0,'370376A',7.75,'C200','S']
df_coppy.loc[df_coppy.shape[0]] = [df_coppy.shape[0]+1,0,3,'BBBB','male',32.0,0,0,'370376A',7.75,'C200','S']

# delete Rows .drop(index)
df_coppy.drop(891) # need inplace=True to do actual operation on df_coppy
df_coppy.drop(891,inplace=True)

df_coppy.iloc[890]   # df_coppy.iloc[890] is the element 890th of the dataframe
df_coppy.iloc[[890]] # df_coppy.iloc[[890]] is dataframe with the element 890th only

df_coppy.drop(df_coppy.iloc[[892]].index)
df_coppy.drop(df_coppy.iloc[[892]].index,inplace=True)
df_coppy.drop(df_coppy.iloc[[891,892]].index,inplace=True)
df_coppy.drop(df_coppy.iloc[[df_coppy.shape[0]-1]].index,inplace=True)
df_coppy.tail()

df_coppy['Age']>30 # conditional
df_coppy[df_coppy['Age']>30] # is the datafram with the elements passing the conditional
df_coppy[df_coppy['Age']>30].index # list of index
df_coppy.drop(df_coppy[df_coppy['Age']>30].index,inplace=True)

# add, delete column
df_coppy["newCol"] = pd.Series(np.random.randn(df_coppy.shape[0]))
df_coppy.head()
del df_coppy["newCol"]
df_coppy.head()





