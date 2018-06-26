def get_products_of_all_ints_except_at_index(lst):

    # Make a list with the products
    if len(lst)<2:
        raise ValueError()
    
    res = [None]*len(lst)
    
    psf = 1
    for i in range(len(lst)):
        res[i] = psf
        psf *= lst[i]
    
    psf=1
    for i in range(len(lst)-1,-1,-1):
        res[i] *= psf
        psf *= lst[i]
    
    return res

# Tests


actual = get_products_of_all_ints_except_at_index([1, 2, 3])
expected = [6, 3, 2]
print(actual == expected)

actual = get_products_of_all_ints_except_at_index([8, 2, 4, 3, 1, 5])
expected = [120, 480, 240, 320, 960, 192]
print(actual == expected)

actual = get_products_of_all_ints_except_at_index([6, 2, 0, 3])
expected = [0, 0, 36, 0]
print(actual == expected)

actual = get_products_of_all_ints_except_at_index([4, 0, 9, 1, 0])
expected = [0, 0, 0, 0, 0]
print(actual == expected)

actual = get_products_of_all_ints_except_at_index([-3, 8, 4])
expected = [32, -12, -24]
print(actual == expected)

actual = get_products_of_all_ints_except_at_index([-7, -1, -4, -2])
expected = [-8, -56, -14, -28]
print(actual == expected)