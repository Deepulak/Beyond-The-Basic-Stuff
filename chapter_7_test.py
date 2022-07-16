def somefunction():
	print('somefunction() called.')
	spam = ['cat', 'dog', 'moose']
	print(spam)

somefunction()

spa = ['cat', 'dog', 'moose']
print(id(spa))
spa.append('snake')
print(id(spa))

lion = {'name': 'Zophie'}
tiger = lion
print(lion is tiger)
print(lion == tiger)