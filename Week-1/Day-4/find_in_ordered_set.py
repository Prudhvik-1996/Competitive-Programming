def contains(lst, key):
    
    l = 0
    h = len(lst)-1
    
    if lst == []:
        return False
        
    # Check if an integer is present in the list
    while l<=h:
        mid = l + ((h-l)/2)
        if key<lst[mid]: h = mid-1
        elif key>lst[mid]: l = mid+1
        else: return True

    return False

# Tests

result = contains([], 1)
expected = False
print(result == expected)

result = contains([1], 1)
expected = True
print(result == expected)

result = contains([1], 2)
expected = False
print(result == expected)

result = contains([2, 4, 6], 4)
expected = True
print(result == expected)

result = contains([2, 4, 6], 5)
expected = False
print(result == expected)

result = contains([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 8)
expected = True
print(result == expected)

result = contains([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0)
expected = False
print(result == expected)

result = contains([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1)
expected = True
print(result == expected)

result = contains([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10)
expected = True
print(result == expected)