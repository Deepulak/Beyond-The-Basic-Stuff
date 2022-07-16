nestedList = [[0,1,2,3], [4], [5,6], [7,8,9]]
flatList = [num for sublist in nestedList for num in sublist]
print(flatList)

anonestedList = [[0,1,2,3], [4], [5,6], [7,8,9]]
anoflatList = []
for sublist in anonestedList:
	for num in sublist:
		anoflatList.append(num)

print(anoflatList)