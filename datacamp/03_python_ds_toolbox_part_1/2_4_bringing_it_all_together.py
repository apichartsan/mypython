# Import pandas
import pandas as pd

# Import Twitter data as DataFrame: df
tweets_df = pd.read_csv('tweets.csv')

# you've just generalized your Twitter language analysis that you did in the previous chapter to include a default argument for the column name. 

# Define count_entries()
def count_entries(df, col_name='lang'):
	"""Return a dictionary with counts of
	occurrences as value for each key."""

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
result1 = count_entries(tweets_df)

# Call count_entries(): result2
result2 = count_entries(tweets_df, 'source')

# Print result1 and result2
print(result1)
print(result2)



# You're now going to generalize this function one step further by allowing the user to pass it a flexible argument, that is, in this case, as many column names as the user would like!

# Define count_entries()
def count_entries(df, *args):
	"""Return a dictionary with counts of
	occurrences as value for each key."""

	#Initialize an empty dictionary: cols_count
	cols_count = {}

	# Iterate over column names in args
	for col_name in args:

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

# Call count_entries(): result2
result2 = count_entries(tweets_df, 'lang', 'source')

# Print result1 and result2
print(result1)
print(result2)


