


if False:
	## Suppose that you have 2 quantities linked togther like countries and their populations.
	## You can represent them as 2 lists, with the name of countries comes in the same order as the corresponding population.

	countries = ["afghanistan","albania","algeria"]
	pop = [30.55, 2.77, 39.21]  # in million unit

	# Then the population can be retrieved by:
	afgan_pop = pop[countries.index('afghanistan')]

	# This is obviously NOT convenient, and NOT intuitive

	## We can use dictionary { key1:value1, key2:value2, ...}
	world = {"afghanistan":30.55, "albania":2.77, "algeria":39.21}
	print world
	alba_pop = world["albania"]
	print 'The population of Albania is ', alba_pop



if False:
	###------------------------------###
	##  Motivation for dictionaries   ##
	###------------------------------###
	
	# Definition of countries and capital
	countries = ['spain', 'france', 'germany', 'norway']
	capitals = ['madrid', 'paris', 'berlin', 'oslo']

	# Get index of 'germany': ind_ger
	ind_ger = countries.index('germany')
	print ('the index of \'germany\' is: ', ind_ger)
	# Use ind_ger to print out capital of Germany
	print ('the capital of Germany is ', capitals[ind_ger])

	print ('the capital of Germany is ', capitals[countries.index('germany')])



if False:
	###------------------------------###
	##  Dictionary Creation           ##
	###------------------------------###
	
	### The countries and capitals lists are again available in the script. It's your job to convert this data to a dictionary where the country names are the keys and the capitals are the corresponding values. As a refresher, here is a recipe for creating a dictionary:
	#my_dict = {
	#	"key1":"value1",
	#		"key2":"value2",
	#}
	###-----
	
	# Definition of countries and capital
	countries = ['spain', 'france', 'germany', 'norway']
	capitals = ['madrid', 'paris', 'berlin', 'oslo']

	# From string in countries and capitals, create dictionary europe
	europe = { 'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }
	# Print europe
	print (europe)

	## Check out which keys are in europe by calling the keys() method on europe. Print out the result.
	# Print out the keys in europe
	print (europe.keys())

	# Print out value that belongs to key 'norway'
	print (europe['norway'])
	
	###------------------------------###
	##  Dictionary Manipulation (1)   ##
	###------------------------------###

	## If you know how to access a dictionary, you can also assign a new value to it. To add a new key-value pair to europe you can use something like this:
	##europe['iceland'] = 'reykjavik'

	# Add italy to europe
	europe['italy'] = 'rome'

	#To assert that 'italy' is now a key in europe
	# Print out italy in europe
	print('italy' in europe) ## True/False
	#print (europe)
	#print (europe['italy'])

	# Add poland to europe
	europe['poland'] = 'warsaw'

	# Print europe
	print (europe)

if False:
	###------------------------------###
	##  Dictionary Manipulation (2)   ##
	###------------------------------###

	##Somebody thought it would be funny to mess with your accurately generated dictionary. An adapted version of the europe dictionary is available in the script on the right.

	##Can you clean up? Do not do this by adapting the definition of europe, but by adding Python commands to the script to update and remove key:value pairs.

	# Definition of dictionary
	europe = {'spain':'madrid', 'france':'paris', 'germany':'bonn',
		'norway':'oslo', 'italy':'rome', 'poland':'warsaw',
			'australia':'vienna' }
	print (europe)

	# Update capital of germany
	europe['germany'] = 'berlin'

	# Australia is not in Europe, Austria is! Remove the key 'australia' from europe
	# Remove australia
	del(europe['australia'])

	# Print europe
	print (europe)

if True:
	###------------------------------###
	##  Dictionary of dictionaries    ##
	###------------------------------###

	# Dictionary of dictionaries
	europe = { 'spain': { 'capital':'madrid', 'population':46.77 },
		'france': { 'capital':'paris', 'population':66.03 },
			'germany': { 'capital':'berlin', 'population':80.62 },
				'norway': { 'capital':'oslo', 'population':5.084 } }


	# Print out the capital of France
	print (europe['france']['capital'])

	# Create sub-dictionary data
	data = {'capital':'rome','population':59.83}

	# Add data to europe under key 'italy'
	europe['italy'] = data

	# Print europe
	print ('italy' in europe )
	print (europe)






