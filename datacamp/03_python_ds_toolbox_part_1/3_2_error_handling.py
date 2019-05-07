
if False:
	##---------------------------------------##
	##   Error handling with try-except      ##
	##---------------------------------------##
	# except >> prevent the program abort, print out a message instead
	# Define shout_echo
	def shout_echo(word1, echo=1):
		"""Concatenate echo copies of word1 and three
		exclamation marks at the end of the string."""

		# Initialize empty strings: echo_word, shout_words
		echo_word = ''
		shout_words = 'DEFAULT'

		# Add exception handling with try-except
		try:
		## If there is exception during a line, the program will skip the rest of the code in this block onto the except block
			# Concatenate echo copies of word1 using *: echo_word
			echo_word = word1*echo

			# Concatenate '!!!' to echo_word: shout_words
			shout_words = echo_word + '!!!'
		except:
			# Print error message
			print("word1 must be a string and echo must be an integer.")

		# Return shout_words
		return shout_words

	# Call shout_echo
	a = shout_echo("particle", echo="accelerator")
	print a


##---------------------------------------##
##   Error handling by raising an error  ##
##---------------------------------------##
if False:
	# Define shout_echo
	def shout_echo(word1, echo=1):
		"""Concatenate echo copies of word1 and three
		exclamation marks at the end of the string."""

		# Initialize empty strings: echo_word, shout_words
		echo_word = ''
		shout_words = 'DEFAULT'

		# Raise an error with raise
		if echo < 0:
			raise ValueError('echo must be greater than 0')
			# this will abort the program

		# Concatenate echo copies of word1 using *: echo_word
		echo_word = word1 * echo
		### here str * (-1) is syntactically correct, so normally there is no error caugh, hence no error raised. We can use 'raise' to define what will be raised in our function.

		# Concatenate '!!!' to echo_word: shout_word
		shout_word = echo_word + '!!!'

		# Return shout_word
		return shout_word

	# Call shout_echo
	a = shout_echo("particle", echo=-1)
	print a


