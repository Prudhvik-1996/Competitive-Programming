def reconstructQueue(lst):
	lst.sort(key=lambda (h,k):(-h,k))
	# print lst
	result = []
	for p in lst:
		# print result
		result.insert(p[1], p)
	# print result
	return result

actual = reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]])
expected = [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
print actual == expected

actual = reconstructQueue([[12,0], [6,3], [3,4], [9,2], [11,1], [1,5]])
expected = [[12,0], [11,1], [9,2], [6,3], [3,4], [1,5]]
print actual == expected

actual = reconstructQueue([[2,4], [5,1], [3,3], [1,5], [4,2], [6,0]])
expected = [[6,0], [5,1], [4,2], [3,3], [2,4], [1,5]]
print actual == expected