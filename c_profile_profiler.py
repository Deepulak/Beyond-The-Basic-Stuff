import time, cProfile

def addUpNumbers():
	total = 0
	for i in range(1, 1000001):
		total += i 

cProfile.run('addUpNumbers()')