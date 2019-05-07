

if False:
	# Define three_shouts
	def three_shouts(word1, word2, word3):
		"""Returns a tuple of strings
		concatenated with '!!!'."""

		# Define inner
		def inner(word):
			"""Returns a string concatenated with '!!!'."""
			return word + '!!!'

		# Return a tuple of strings
		return (inner(word1), inner(word2), inner(word3))

		# Call three_shouts() and print
	print(three_shouts('a', 'b', 'c'))


	# here the funtion 'three_shouts(word1, word2, word3)' is called 'enclosing scope'
	# and the function 'inner(word)' is called 'nested or inner function'
	# One other pretty cool reason for nesting functions is the idea of a closure. This means that the nested or inner function remembers the state of its enclosing scope when called. Thus, anything defined locally in the enclosing scope is available to the inner function even when the outer function has finished execution. ??

if False:
	# Define echo
	def echo(n):
		"""Return the inner_echo function."""
			
		# Define inner_echo
		def inner_echo(word1):
			"""Concatenate n copies of word1."""
			echo_word = word1 * n
			return echo_word

		# Return inner_echo
		return inner_echo ### Notice that the function echo(n) returns 'a function'

	# Call echo: twice
	twice = echo(2)

	# Call echo: thrice
	thrice = echo(3)

	# Call twice() and thrice() then print
	print(twice('hello'), thrice('hello'))



#if False:
#	This is about using the keyword 'nonlocal' which is not avalable in python 2.7
#	# Define echo_shout()
#	def echo_shout(word):
#		"""Change the value of a nonlocal variable"""
#			
#		# Concatenate word with itself: echo_word
#		echo_word = word*2
#
#		# Print echo_word
#		print(echo_word)
#
#		# Define inner function shout()
#		def shout():
#			"""Alter a variable in the enclosing scope"""
#			# Use echo_word in nonlocal scope
#			nonlocal echo_word
#           # usually what is within a function is separate from outside but in python3 you can use 'nonlocal' to connect local with the 'enclosing scope'
#			# this is analog to what is done when you want to access and alter the 'global'
#
#			# Change echo_word to echo_word concatenated with '!!!'
#			echo_word = echo_word + '!!!'
#
#		# Call function shout()
#		shout()
#
#		# Print echo_word
#		print(echo_word)
#
#	# Call function echo_shout() with argument 'hello'
#	echo_shout('hello')




