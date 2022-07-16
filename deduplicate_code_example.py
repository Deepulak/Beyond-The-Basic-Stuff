def askFeeling(timeOfDay):
	print('good ' + timeOfDay + '.')
	print('How are you feeling?')
	feeling = input()
	print('I am happy to hear that you are feeling ' + feeling + '.')

for timeOfDay in ['morning', 'afternoon', 'evening']:
	askFeeling(timeOfDay)