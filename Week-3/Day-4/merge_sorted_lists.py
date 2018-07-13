def merge_lists(my_list, alices_list):

    # Combine the sorted lists into one large sorted list
    l = []
    i = 0
    j = 0
    
    if my_list == []:
        return alices_list
    
    if alices_list == []:
        return my_list
    
    while i<len(my_list) and j<len(alices_list):
        if my_list[i] < alices_list[j]:
            l.append(my_list[i])
            i += 1
        else:
            l.append(alices_list[j])
            j += 1
    
    while i==len(my_list)-1:
        l.append(my_list[i])
        i += 1
    
    while j==len(alices_list)-1:
        l.append(alices_list[j])
        j += 1

    return l

# Tests

actual = merge_lists([], [])
expected = []
print(actual == expected)

actual = merge_lists([], [1, 2, 3])
expected = [1, 2, 3]
print(actual == expected)

actual = merge_lists([5, 6, 7], [])
expected = [5, 6, 7]
print(actual == expected)

actual = merge_lists([2, 4, 6], [1, 3, 7])
expected = [1, 2, 3, 4, 6, 7]
print(actual == expected)

actual = merge_lists([2, 4, 6, 8], [1, 7])
expected = [1, 2, 4, 6, 7, 8]
print(actual == expected)