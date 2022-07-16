import timeit
a, b = 42, 101	# Set up the two variables.
print(a, b)

# A series of ^ XOR operations will end up
# swapping their values.

a = a ^ b
b = a ^ b
a = a ^ b
print(a, b)  	# The values are now swapped.
timeit.timeit('print(a, b)', number=1, globals=globals())