class ClassWithBadProperty:
	def __init__(self):
		self.someAttribute = 'some initial value'

	@property
	def someAttribute(self): # This
		# We forgot the _ underscore
		# us to use the property and
		return self.someAttribute #

	@someAttribute.setter
	def someAttribute(self, value):
		self._someAttribute = value

# This is the "setter" method.
obj = ClassWithBadProperty()
print(obj.someAttribute) # Error because the getter calls the getter.