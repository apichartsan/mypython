# Import pandas
import pandas as pd


if False:
	# Import Twitter data as DataFrame: df
	df = pd.read_csv('tweets.csv')

	# Initialize an empty dictionary: langs_count
	langs_count = {}

	# Extract column from DataFrame: col
	col = df['lang']

	# Iterate over lang column in DataFrame
	for entry in col:
		
		# If the language is in langs_count, add 1
		if entry in langs_count.keys():
			langs_count[entry] = langs_count[entry] + 1
		# Else add the language to langs_count, set the value to 1
		else:
			langs_count[entry] = 1

	# Print the populated dictionary
	print(langs_count)

	# additional
	print df['lang'].value_counts()
	print df['lang'].value_counts()[0]
	print df['lang'].value_counts()[1]
	print df['lang'].value_counts()[2]

	# note that in tweets.csv, the column 'place' has the value as a string representation of a dictionary, see https://stackoverflow.com/questions/988228/convert-a-string-representation-of-a-dictionary-to-a-dictionary


# Define count_entries()
def count_entries(df, col_name):
	"""Return a dictionary with counts of
	occurrences as value for each key."""

	# Initialize an empty dictionary: langs_count
	langs_count = {}

	# Extract column from DataFrame: col
	col = df[col_name]

	# Iterate over lang column in DataFrame
	for entry in col:

		# If the language is in langs_count, add 1
		if entry in langs_count.keys():
			langs_count[entry] = langs_count[entry]+1
		# Else add the language to langs_count, set the value to 1
		else:
			langs_count[entry] = 1

	# Return the langs_count dictionary
	return langs_count


# Import Twitter data as DataFrame: df
tweets_df = pd.read_csv('tweets.csv')

# Call count_entries(): result
result = count_entries(tweets_df, 'lang')

# Print the result
print(result)


