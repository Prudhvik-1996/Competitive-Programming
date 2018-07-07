def is_single_riffle(half1, half2, shuffled_deck):

    # Check if the shuffled deck is a single riffle of the halves
    l1 = len(half1)
    l2 = len(half2)
    l = len(shuffled_deck)
    
    h1i = 0
    h2i = 0
    
    if l1 + l2 != l:
        return False
    
    for i in shuffled_deck:
        if h1i<l1 and i==half1[h1i]:
            h1i += 1
        elif h2i<l2 and i==half2[h2i]:
            h2i += 1
        elif i!=half1[h1i] or i!=half2[h2i]:
            return False
        
    return True

# Tests

result = is_single_riffle([1, 4, 5], [2, 3, 6], [1, 2, 3, 4, 5, 6])
expected = True
print(result == expected)

result = is_single_riffle([1, 5], [2, 3, 6], [1, 2, 6, 3, 5])
expected = False
print(result == expected)

result = is_single_riffle([], [2, 3, 6], [2, 3, 6])
expected = True
print(result == expected)

result = is_single_riffle([1, 5], [2, 3, 6], [1, 6, 3, 5])
expected = False
print(result == expected)

result = is_single_riffle([1, 5], [2, 3, 6], [1, 2, 3, 5, 6, 8])
expected = False
print(result == expected)