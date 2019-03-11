import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

from sklearn.metrics import confusion_matrix


#	Logistic regression
#	- used for binary classification problem
#	- the outout of logistic regression is the prob to be success from 0 to 1
#	- this is guided by Sigmoid function >> p = sigmoid( theta_transpose * X )
#	- p <  0.5 class 0
#	- p >= 0.5 class 1


# The goal is t opredict 'servival' from the 'fare'
# Set default Seaborn style
sns.set()

df = pd.read_csv('titanic_data.csv')
df.head() #  This will let you identify which column names

##------------------------------
##  now actaul train model : using 1 feature
##------------------------------
df_pre = df.copy()
df_test = df_pre[['Fare','Survived']]
df_test.dropna(inplace=True)

x = df_test[['Fare']]
y = df_test[['Survived']]
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.5)

logis_model = linear_model.LogisticRegression()
logis_model.fit(x_train,y_train)
y_pred = logis_model.predict(x_test)

_ = plt.scatter(x_train,y_train, color='blue', alpha = 0.5)
_ = plt.scatter(x_test,y_test, color='green', alpha = 0.5)
_ = plt.scatter(x_test,y_pred, color='red', alpha = 0.5)
plt.show()

# to assess accuracy of the model in classification problem
# we look at correct-identification rate (or "Accuracy")
rate = np.sum(y_pred == y_test['Survived'])/float(len(y_pred))

print 'Correct ID Rate: ', rate
# Correct ID Rate:  0.6771300448430493
# OK this is a bit better than random (0.5)
# but how do we justify this value
# we compare it to the performance of some simple model >> benchmark

# How about we use some basic social assumption like "lady first" >> so we predict that all women survive
df_pre = df.copy()
df_pre['Dummy'] = 0
df_pre.loc[df_pre['Sex'] == 'female'] = 1
print (df_pre['Dummy'] == df_pre['Survived']).mean()
# 0.877665544332211
# This simple model is better than our model

##------------------------------
##  using >1 feature
##------------------------------

df_pre = df.copy()
df_test = df_pre[['Fare','Age','Pclass','SibSp','Parch','Survived']]
df_test.dropna(inplace=True)

x = df_test[['Fare','Age','Pclass','SibSp','Parch']]
y = df_test[['Survived']]
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.5)

logis_model = linear_model.LogisticRegression()
logis_model.fit(x_train,y_train)
y_pred = logis_model.predict(x_test)

# to assess accuracy of the model in classification problem
# we look at correct-identification rate
rate = np.sum(y_pred == y_test['Survived'])/float(len(y_pred))
print 'Correct ID Rate: ', rate
# Correct ID Rate:  0.7310924369747899
# Now this is getting better but we know that SEX is the strong discriminant feature so we certatinly want to include it >> need to encode it in to mnumber like Sex_num


##------------------------------
##  confusion_matrix
##------------------------------

cm = confusion_matrix(y_test, y_pred)
tn,fp,fn,tp = cm.ravel()



