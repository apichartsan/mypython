# Import pandas
import pandas as pd



# Import Twitter data as DataFrame: df
tweets_df = pd.read_csv('tweets.csv')


if False:
	# (1)
	# This is awesome! You have now learned how to write anonymous functions using lambda, how to pass lambda functions as arguments to other functions such as map(), filter(), and reduce(), as well as how to write errors and output custom error messages within your functions. You will now put together these learnings to good use by working with a Twitter dataset. Before practicing your new error handling skills,in this exercise, you will write a lambda function and use filter() to select retweets, that is, tweets that begin with the string 'RT'.

	# To help you accomplish this, the Twitter data has been imported into the DataFrame, tweets_df. Go for it!

	# Select retweets from the Twitter DataFrame: result
	result = filter(lambda x: x[0:2]=='RT', tweets_df['text'])

	# Create list from filter object result: res_list
	res_list = list(result)

	# Print all retweets in res_list
	for tweet in res_list:
		print(tweet)


if False:
	# (2)
	# Sometimes, we make mistakes when calling functions - even ones you made yourself. But don't fret! In this exercise, you will improve on your previous work with the count_entries() function in the last chapter by adding a try-except block to it. This will allow your function to provide a helpful message when the user calls your count_entries() function but provides a column name that isn't in the DataFrame.

	# Define count_entries()
	def count_entries(df, col_name='lang'):
		"""Return a dictionary with counts of
		occurrences as value for each key."""

		# Initialize an empty dictionary: cols_count
		cols_count = {}

		# Add try block
		try:
			# Extract column from DataFrame: col
			col = df[col_name]

			# Iterate over the column in dataframe
			for entry in col:

				# If entry is in cols_count, add 1
				if entry in cols_count.keys():
					cols_count[entry] += 1
				# Else add the entry to cols_count, set the value to 1
				else:
					cols_count[entry] = 1

			# Return the cols_count dictionary
			return cols_count

		# Add except block
		except:
			print("The DataFrame does not have a '" + col_name + "' column.")

	# Call count_entries(): result1
	#result1 = count_entries(tweets_df, 'la')
	result1 = count_entries(tweets_df, 'lang')

	# Print result1
	print(result1)
	##  note that this function can actually be achieved by tweets_df['lang'].value_counts()['en']
	print(tweets_df['lang'].value_counts())




# In the previous exercise, you built on your function count_entries() to add a try-except block. This was so that users would get helpful messages when calling your count_entries() function and providing a column name that isn't in the DataFrame. In this exercise, you'll instead raise a ValueError in the case that the user provides a column name that isn't in the DataFrame.


# Define count_entries()
def count_entries(df, col_name='lang'):
	"""Return a dictionary with counts of
	occurrences as value for each key."""

	# Raise a ValueError if col_name is NOT in DataFrame
	if col_name not in df.columns:
		raise ValueError ('The DataFrame does not have a "' + col_name + '" column.')

	# Initialize an empty dictionary: cols_count
	cols_count = {}

	# Extract column from DataFrame: col
	col = df[col_name]

	# Iterate over the column in DataFrame
	for entry in col:

		# If entry is in cols_count, add 1
		if entry in cols_count.keys():
			cols_count[entry] += 1
		# Else add the entry to cols_count, set the value to 1
		else:
			cols_count[entry] = 1

	# Return the cols_count dictionary
	return cols_count

# Call count_entries(): result1
result1 = count_entries(tweets_df, 'lang')

# Print result1
print(result1)
