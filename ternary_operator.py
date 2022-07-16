valueIfTrue = 'Access Granted'
valueIfFalse = 'Access Denied'
condition = True
message = valueIfTrue if condition else valueIfFalse
print(message)
print(valueIfTrue if condition else valueIfFalse)
condition = False
message = valueIfTrue if condition else valueIfFalse
print(message)
condition = True
condition and valueIfTrue or valueIfFalse
print(condition)
# unpythonic example
age = 30
ageRange = 'child' if age < 13 else 'teenager' if age >= 13 and age < 18 else 'adult'
print(ageRange)

# unpythonic example
#if 42 < spam and spam < 99:
# pythonic example
#if 42 < spam < 99:
