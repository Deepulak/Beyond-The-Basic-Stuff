try:
	name = input('Enter a name: ')
	name = str(name)
except ValueError:
	pass

# another type of exception
try:
	num = input("Enter a number: ")
	num = int(num)
except ValueError:
	print('An incorrect value was passed to int()')