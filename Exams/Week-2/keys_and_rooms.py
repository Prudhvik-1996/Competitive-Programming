def canWalkThrough(l):
	ls = []
	for i in range(len(l)-1):
		ls.extend(l[i])
		if i+1 not in ls:
			return False
	return True

expected = True
actual = canWalkThrough([[1], [0,2], [3]])
print actual == expected

expected = False
actual = canWalkThrough([[1,3], [3,0,1], [2], [0]])
print actual == expected

expected = True
actual = canWalkThrough([[1,2,3], [0], [0], [0]])
print actual == expected

expected = True
actual = canWalkThrough([[1], [0,2,4], [1,3,4], [2], [1,2]])
print actual == expected

expected = False
actual = canWalkThrough([[1], [2,3], [1,2], [4], [1], [5]])
print actual == expected

expected = True
actual = canWalkThrough([[1], [2], [3], [4], [2]])
print actual == expected

expected = False
actual = canWalkThrough([[1], [1,3], [2], [2,4,6], [], [1,2,3], [1]])
print actual == expected