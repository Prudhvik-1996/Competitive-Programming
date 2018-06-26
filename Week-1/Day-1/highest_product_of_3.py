def highest_product_of_3(lst):

    # Calculate the highest product of three numbers
    if len(lst)<3:
        raise ValueError()
    
    h = max(lst[0],lst[1])
    l = min(lst[0],lst[1])
    
    h2 = lst[0]*lst[1]
    l2 = lst[0]*lst[1]
    
    h3 = lst[0]*lst[1]*lst[2]
    
    for i in range(2,len(lst)):
        current = lst[i]
        
        h3 = max(h3,current*h2,current*l2)
        
        h2 = max(h2,current*h,current*l)
        l2 = min(l2,current*h,current*l)
        
        h = max(h,current)
        l = min(l,current)
        
    return h3

# Tests

actual = highest_product_of_3([1, 2, 3, 4])
expected = 24
print(actual == expected)

actual = highest_product_of_3([6, 1, 3, 5, 7, 8, 2])
expected = 336
print(actual == expected)

actual = highest_product_of_3([-5, 4, 8, 2, 3])
expected = 96
print(actual == expected)

actual = highest_product_of_3([-10, 1, 3, 2, -10])
expected = 300
print(actual == expected)

actual = highest_product_of_3([-5, -1, -3, -2])
expected = -6
print(actual == expected)