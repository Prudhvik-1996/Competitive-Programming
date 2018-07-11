def find_duplicate(arr):

    # Find a number that appears more than once ... in O(n) time
#     for i in range(0, len(arr)):
#         if arr[abs(arr[i])] >= 0:
#             arr[abs(arr[i])] = -arr[abs(arr[i])]
#         else:
#             return abs(arr[i])

#     return 0

    n = len(list)
    i = n
    j = n
    while True:
#         print("looking for cycle: i %s j %s" % (i, j))
        i = list[i - 1]  # tortoise
        j = list[j - 1]  # hare
        j = list[j - 1]  # hare
        if i == j:
#             print("cycle found at %s" % i)
            break

    # we found a cycle
    # now restart j
    # and loop until j meets i again
    # and that's the start of the cycle (or the dup)

    j = n
    while True:
#         print("looking for dup: i %s j %s" % (i, j))
        i = list[i - 1]
        j = list[j - 1]
        if i == j:
#             print("dup found at %s" % i)
            break

#     print("dup is %s" % i)
    return i

# Tests

actual = find_duplicate([1, 1])
expected = 1
print(actual == expected)

actual = find_duplicate([1, 2, 3, 2])
expected = 2
print(actual == expected)

actual = find_duplicate([1, 2, 5, 5, 5, 5])
expected = 5
print(actual == expected)

actual = find_duplicate([4, 1, 4, 8, 3, 2, 7, 6, 5])
expected = 4
print(actual == expected)
