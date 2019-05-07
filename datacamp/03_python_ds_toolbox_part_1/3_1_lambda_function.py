
##---------------------------------------##
##   Introduction : lambda               ##
##---------------------------------------##
if False:
	# Pop quiz on lambda functions
	add_bangs = (lambda a: a + '!!!')
	print add_bangs('hello')


if False:
	# Define echo_word as a lambda function: echo_word
	echo_word = (lambda word1, echo: word1 * echo)

	# Call echo_word: result
	result = echo_word('hey', 5)

	# Print result
	print(result)


##---------------------------------------##
##   map() and lambda functions          ##
##---------------------------------------##
#	>> map() is abuilt-in function
if False:
	nums = [2, 4, 6, 8, 10]
	result = map(lambda a: a ** 2, nums)
	# The map object that results from the call to map() is stored in result
	print (nums)
	print (result)

if False:
	# Create a list of strings: spells
	spells = ["protego", "accio", "expecto patronum", "legilimens"]

	# Use map() to apply a lambda function over spells: shout_spells
	shout_spells = map(lambda item: item + '!!!', spells)

	# Convert shout_spells to a list: shout_spells_list
	shout_spells_list = list(shout_spells)

	# Convert shout_spells into a list and print it
	print(shout_spells_list)



##---------------------------------------##
##   Filter() and lambda functions       ##
##---------------------------------------##
if False:
	# Pop quiz on lambda functions
	add_bangs = (lambda a: a + '!!!')
	print add_bangs('hello')


if False:
	# Create a list of strings: fellowship
	fellowship = ['frodo', 'samwise', 'merry', 'pippin', 'aragorn', 'boromir', 'legolas', 'gimli', 'gandalf']
	
	# Use filter() to apply a lambda function over fellowship: result
	result = filter(lambda a: len(a)>6, fellowship)
	print (type(result))
	
	# Convert result to a list: result_list
	result_list = list(result)
	
	# Convert result into a list and print it
	print(result_list)


##---------------------------------------##
##   Reduce() and lambda functions       ##
##---------------------------------------##
# using reduce() and a lambda function that concatenates strings together.

# Import reduce from functools
from functools import reduce

# Create a list of strings: stark
stark = ['robb', 'sansa', 'arya', 'brandon', 'rickon']

# Use reduce() to apply a lambda function over stark: result
result = reduce(lambda item1,item2: item1+item2, stark)

# Print the result
print(result)





