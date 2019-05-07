

if False:
	x = 4.89
	y1 = str(x)
	#y2 = print(x) # this causes SyntaxError in python 2.7
	print type(x), type(y1)#, type(y2)


# Define shout with the parameter, word
def shout(word):
	"""Return a string with three exclamation marks"""
	# Concatenate the strings: shout_word
	shout_word = word + '!!!'

	# Replace print with return
	return shout_word

# Pass 'congratulations' to shout: yell
yell = shout('congratulations')

# Print yell
print (yell)

# Great work! Here it made sense to assign the output of shout('congratulations') to a variable yell because the function shout actually returns a value, it does not merely print one.

# Define shout with parameters word1 and word2
def shout(word1, word2):
	"""Concatenate strings with three exclamation marks"""
	# Concatenate word1 with '!!!': shout1
	shout1 = word1 + '!!!'

	# Concatenate word2 with '!!!': shout2
	shout2 = word2 + '!!!'

	# Concatenate shout1 with shout2: new_shout
	new_shout = shout1 + shout2

	# Return new_shout
	return new_shout

# Pass 'congratulations' and 'you' to shout(): yell
yell = shout('congratulations', 'you')

# Print yell
print(yell)