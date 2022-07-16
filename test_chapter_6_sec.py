fileObj = open('spam.txt', 'w')
fileObj.write('Hello World!')
fileObj.close()

with open('spam_2.txt', 'w') as fileObj_sec:
	fileObj_sec.write('Fuck u!')

class SomeClass:
	def __eq__(self, other):
		if other is None:
			return True
spam = SomeClass()
spam == None
spam is None