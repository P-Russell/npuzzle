def find_item(theList, item):
	return [(ind, theList[ind].index(item))
	for ind in range(len(theList))
	if item in theList[ind]]
