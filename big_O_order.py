def readingList(books):
	print('Here are the books I will read : ')
	numberOfBooks = 0
	for book in books:
		print(book)
		numberOfBooks += 1
	print(numberOfBooks, 'books total')