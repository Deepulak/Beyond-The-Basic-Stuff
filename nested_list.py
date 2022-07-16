nestedIntList = [[0,1,2,3], [4], [5,6], [7,8,9]]
nestedStrList = [[str(i) for i in sublist] for sublist in nestedIntList]
print(nestedStrList)

anoNestedIntList = [[0,1,2,3], [4], [5,6], [7,8,9]]
anoNestedStrList = []
for sublist in anoNestedIntList:
	anoNestedStrList.append([str(i) for i in sublist])
print(anoNestedStrList)