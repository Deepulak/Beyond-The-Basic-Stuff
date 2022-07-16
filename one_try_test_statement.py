import os

def detectWithConfirmation(filename):
	try:
		if (input('Delete ' + filename + ', are you sure? Y/N') == 'Y'):
			os.unlink(filename)
	except FileNotFoundError:
		print("That file already did not exist.")		