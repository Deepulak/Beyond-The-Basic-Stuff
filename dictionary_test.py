numberOfPets = {'dogs': 2, 'cats': 3}
if 'cats' in numberOfPets:
	print('I have', numberOfPets['cats'], 'cats.')
else:
	print('I have 0 cats.')

# pythonic example
numOfPets = {'dogs': 2}
print('I have', numOfPets.get('cats', 3), 'cats.')

# unpythonic example
pets = {'dogs': 2}
if 'cats' not in pets:
	pets['cats'] = 0

pets['dogs'] += 10
pets['cats'] += 10
print(pets['cats'])
print(pets['dogs'])

# pythonic example
numpets = {'dogs': 2}
numpets.setdefault('cats', 4)

numpets['cats'] += 14
print(numpets['cats'])

# use collections.deafultdict for default values
import collections
scores = collections.defaultdict(int)
print(scores)
# No need to set a value for the 'Al' key first.
scores['Al'] += 1
print(scores)
# No need to set a calue for the 'zophie' key first.
scores['zophie'] 
print(scores)
# add some value on the scores['zophie']dict
scores['Zophie'] += 40 
print(scores)

# collections.defaultdic(list)
booksReadBy = collections.defaultdict(list)
booksReadBy['Al'].append('Oryx and Crake')
booksReadBy['Al'].append('American Gods')
print(len(booksReadBy['Al']))
print(len(booksReadBy['Zophie']))