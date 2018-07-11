def find_repeat(arr):

    # Find a number that appears more than once
    for i in range(0, len(arr)):
        if arr[abs(arr[i])] >= 0:
            arr[abs(arr[i])] = -arr[abs(arr[i])]
        else:
            return abs(arr[i])

# Tests

actual = find_repeat([1, 1])
expected = 1
print(actual == expected)

actual = find_repeat([1, 2, 3, 2])
expected = 2
print(actual == expected)

actual = find_repeat([1, 2, 5, 5, 5, 5])
expected = 5
print(actual == expected)

actual = find_repeat([4, 1, 4, 8, 3, 2, 7, 6, 5])
expected = 4
print(actual == expected)