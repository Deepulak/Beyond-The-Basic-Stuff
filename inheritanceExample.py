class ParentClass:
	def printHello(self):
		print("Hello, World!")

class ChildClass(ParentClass):
	def someNewMethod(self):
		print("ParentClass object don't have this method.")

class GrandchildClass(ChildClass):
	def anotherNewMethod(ChildClass):
		print("Only GrandchildClass object have this method.")

print('Create a ParentClass object and call its method:')
parent = ParentClass()
parent.printHello()

print('Create a ChildClass object and call its method:')
child = ChildClass()
child.printHello()
child.someNewMethod()

print('Create a GrandchildClass object and call its method:')
grandchild = GrandchildClass()
grandchild.printHello()
grandchild.someNewMethod()
grandchild.anotherNewMethod()

print("An Error:")
parent.someNewMethod()