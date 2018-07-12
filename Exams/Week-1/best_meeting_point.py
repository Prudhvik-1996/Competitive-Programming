def minTotalDistance( grid):
	x = []
	for i, row in enumerate(grid):
		for v in row:
			if v==1:
				x.append(i)

	y = []
	for row in grid:
		for j, v in enumerate(row):
			if v==1:
				y.append(j)
	
	if len(x)==0 or len(y)==0: return 0
	mid_x = findKthLargest(x, len(x) / 2 + 1)
	mid_y = findKthLargest(y, len(y) / 2 + 1)

	res = 0
	for i, row in enumerate(grid):
		for j, v in enumerate(row):
			if v==1:
				res += abs(mid_x-i) + abs(mid_y-j)
	return res

def findKthLargest(nums, k):
	nums.sort()
	return nums[k-1]

actual = minTotalDistance([
	[1, 0, 0, 0, 1],
	[0, 0, 0, 0, 0],
	[0, 0, 1, 0, 0]
	])
expected = 6
print actual == expected

actual = minTotalDistance([
	[1, 0, 1, 0, 1],
	[0, 1, 0, 0, 0],
	[0, 1, 1, 0, 0]
	])
expected = 11
print actual == expected

actual = minTotalDistance([
	[1, 1],
	[1, 1]
	])
expected = 4
print actual == expected

actual = minTotalDistance([
	[0, 0],
	[0, 0]
	])
expected = 0
print actual == expected

actual = minTotalDistance([
	[1, 0],
	[0, 0]
	])
expected = 0
print actual == expected

