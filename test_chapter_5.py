import random

def coinFlip():
	if random.randint(0, 1):
		return 'Heads!'
	else:
		return 'Tails!'
	return 'The coin landed on its edge!'

print(coinFlip())