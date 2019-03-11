import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

# Set default Seaborn style
sns.set()

df = pd.read_csv('titanic_data.csv')
df.head() #  This will let you identify which column names

if False:
	##-----------------------------
	##  P.38 linear regression
	##-----------------------------
	# We are going to do linear regression problem
	# Predicting the fare from the age

	df_pre = df.copy()
	#df_test = df_pre[['Age','Fare']]
	df_test = df_pre[['Age','Fare']][:15] # this takes only the the first 15 examples
	# let's drop the examples having value = NAN
	df_test.dropna(inplace=True)
	_ = plt.scatter(df_test['Age'],df_test['Fare'])
	plt.show()

	x = df_test[['Age']]
	y = df_test[['Fare']]

	model = linear_model.LinearRegression()
	model.fit(x,y)
	y_pred = model.predict(x)

	_ = plt.scatter(df_test['Age'],df_test['Fare'])
	_ = plt.plot(df_test['Age'],y_pred, color='red', linewidth=3)
	plt.show()

	print 'Mean Squared Error: ', mean_squared_error(y, y_pred)
	print 'R2 score : ', r2_score(y, y_pred)
	print 'Coefficients of the model: ', model.coef_


	##-----------------------------
	## P.40: train & test set
	##-----------------------------
	df_pre = df.copy()
	df_test = df_pre[['Age','Fare']]
	df_test.dropna(inplace=True)

	testsize = 260
	trainsize = df_test[:-testsize].shape[0]

	# P.42: Random train & test set
	x_train = df_test[['Age']][:-testsize]
	x_test  = df_test[['Age']][testsize:]
	y_train = df_test[['Fare']][:-testsize]
	y_test  = df_test[['Fare']][testsize:]

	model = linear_model.LinearRegression()
	model.fit(x_train,y_train)
	y_pred = model.predict(x_test)

	print 'Mean Squared Error: ', mean_squared_error(y_test, y_pred)
	print 'R2 score : ', r2_score(y_test, y_pred)
	print 'Coefficients of the model: ', model.coef_

	_ = plt.scatter(x_train,y_train, color='blue', alpha = 0.5)
	_ = plt.scatter(x_test,y_test, color='green', alpha = 0.5)
	_ = plt.plot(x_test,y_pred, color='red', linewidth=3)
	plt.show()


##-----------------------------
## P.42: Random train & test set
##-----------------------------
# we want the distribution of train and test be the same

if False:
	# If the data has been sorted, we are doom!
	df_pre = df.copy()
	df_sort = df_pre.sort_values('Pclass')
	df_test = df_sort[['Age','Fare']]
	df_test.dropna(inplace=True)

	testsize = 260
	trainsize = df_test[:-testsize].shape[0]

	# P.42: Random train & test set
	x_train = df_test[['Age']][:-testsize]
	x_test  = df_test[['Age']][testsize:]
	y_train = df_test[['Fare']][:-testsize]
	y_test  = df_test[['Fare']][testsize:]

	model = linear_model.LinearRegression()
	model.fit(x_train,y_train)
	y_pred = model.predict(x_test)

	print 'Mean Squared Error: ', mean_squared_error(y_test, y_pred)
	print 'R2 score : ', r2_score(y_test, y_pred)
	print 'Coefficients of the model: ', model.coef_
	# R2 score :  -8.185923601173554 !!

	#_ = plt.scatter(x_train,y_train, color='blue', alpha = 0.5)
	_ = plt.scatter(x_test,y_test, color='green', alpha = 0.5)
	_ = plt.plot(x_test,y_pred, color='red', linewidth=3)
	plt.show()
	# the prediction is clearly overestimated the price !

	_ = plt.subplot(2,2,1)
	_ = plt.hist(y_train['Fare'], bins=15)
	_ = plt.title('Training Set')
	_ = plt.subplot(2,2,2)
	_ = plt.hist(y_test['Fare'], bins=15)
	_ = plt.title('Test Set')
	plt.show()


	# Let's random it !

	# execise
	df_pre = df.copy()
	df_sort = df_pre.sort_values('Pclass')
	df_test = df_sort[['Age','Fare','Pclass']]
	df_test.dropna(inplace=True)

	x = df_test[['Age','Pclass']]
	y = df_test[['Fare','Pclass']]

	from sklearn.model_selection import train_test_split

	x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.3)
	print x_train.head()


##  now actaul train model
df_pre = df.copy()
df_sort = df_pre.sort_values('Pclass')
df_test = df_sort[['Age','Fare']]
df_test.dropna(inplace=True)

x = df_test[['Age']]
y = df_test[['Fare']]
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.5)

model = linear_model.LinearRegression()
model.fit(x_train,y_train)
y_pred = model.predict(x_test)

print 'Mean Squared Error: ', mean_squared_error(y_test, y_pred)
print 'R2 score : ', r2_score(y_test, y_pred)
print 'Coefficients of the model: ', model.coef_
# R2 score :  0.006970012313119334

#_ = plt.scatter(x_train,y_train, color='blue', alpha = 0.5)
_ = plt.scatter(x_test,y_test, color='green', alpha = 0.5)
_ = plt.plot(x_test,y_pred, color='red', linewidth=3)
plt.show()

# We will have to deal with outliers ( one method is regularization) later. Stay tuned !


