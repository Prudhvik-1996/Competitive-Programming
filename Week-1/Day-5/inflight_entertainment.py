def can_two_movies_fill_flight(movie_lengths, flight_length):

    # Determine if two movie runtimes add up to the flight length
    l = {}
    for x in movie_lengths:
        c = flight_length-x
        if c in l:
            return True
        else:
            l[x] = True

    return False

# Tests

result = can_two_movies_fill_flight([2, 4], 1)
expected = False
print(result == expected)

result = can_two_movies_fill_flight([2, 4], 6)
expected = True
print(result == expected)

result = can_two_movies_fill_flight([3, 8], 6)
expected = False
print(result == expected)

result = can_two_movies_fill_flight([3, 8, 3], 6)
expected = True
print(result == expected)

result = can_two_movies_fill_flight([1, 2, 3, 4, 5, 6], 7)
expected = True
print(result == expected)

result = can_two_movies_fill_flight([6], 6)
expected = False
print(result == expected)

result = can_two_movies_fill_flight([], 2)
expected = False
print(result == expected)
