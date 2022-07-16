def formMolecule(**kwargs):
	if len(kwargs) == 2 and kwargs['hydrogen'] == 2 and kwargs['oxygen'] == 1:
		return 'water'
		# rest of the code for the function goes here
formMolecule(hydrogen=2, oxygen=1)
print(formMolecule(hydrogen=2, oxygen=1))


# Side Effects Function
def removeLastCatFromList(petSpecies):
	if len(petSpecies) > 0 and petSpecies[-1] == 'cat':
		petSpecies.pop()

myPets = ['dog', 'cat', 'bird', 'cat']
removeLastCatFromList(myPets)
print(myPets)

#
# Higher-Order Function
def callItTwice(func, *args, **kwargs):
	func(*args, **kwargs)
	func(*args, **kwargs) 
callItTwice(print, "Hello world!")


# Lambda Function
def rectanglePerimeter(rect):
	return (rect[0] * 2) + (rect[1] * 2)

myRectangle = [4, 10]
print(rectanglePerimeter(myRectangle))


# ############ test ###########
import random

#def returnTwoTypes():
#	if random.randint(1, 2) == 1:
#		return 42
#	else:
#		return "forty two"

#hexNum = hex(returnTwoTypes())
#print(hexNum)

def sometimesReturnsNone():
	if random.randint(1, 2) == 1:
		return "Hello"
	else:
		return None

returnVal = sometimesReturnsNone()
#returnVal.upper()
print(returnVal.upper())