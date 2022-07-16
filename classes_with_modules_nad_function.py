import random

class Dice:
	def __init__(self, sides=6):
		self.sides = sides
	def roll(self):
		return random.randint(1, self.sides)

d = Dice()
print("You rolled a ", d.roll())

print('You rolled a ', random.randint(1, 6))