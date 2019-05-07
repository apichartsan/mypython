

if False:
	new_val = 10 # doing this means it is global
	
	def square_v1(value):
		new_val = (value ** 2) # 'new_val' here is local, unrelated to the global 'new_val'
		return new_val
	
	def square(value):
		new_val_2 = (new_val ** 2) + value # so 'new_val' here is global, can be access anywhere, but can not be reassign
		return new_val_2
	
	
	print square_v1(3)
	print square(3)
	print new_val
	## All above is the concept I already had in mind


if False:
	# Now if you want to alter the global 'new_val', you can do it by calling global
	
	new_val = 10 # doing this means it is global
	
	def square_v3(value):
		global new_val
		new_val = (value ** 2) + new_val # 'new_val' here is the global one
		return new_val
	
	print square_v3(3)
	print new_val
	print square_v3(4)
	print new_val



if False:
	# Create a string: team
	team = "teen titans"

	# Define change_team()
	def change_team():
		"""Change the value of the global variable team."""

		# Use team in global scope
		global team

		# Change the value of team in global: team
		team = 'justice league'

	# Print team
	print(team)

	# Call change_team()
	change_team()

	# Print team
	print(team)


if False:
	import builtins
	#  to print a list of all the names in the module builtins
	dir(builtins)



