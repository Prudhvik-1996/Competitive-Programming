def minimumSwapsCouples(lst):
    n = len(lst)//2

    couples = [[] for _ in range(n)]
    

    for seat, num in enumerate(lst):
        couples[num//2].append(seat//2)
        
    adj = [[] for _ in range(n)]
    
    for seat1, seat2 in couples:
        adj[seat1].append(seat2)
        adj[seat2].append(seat1)

    result = 0
    
    for seat in range(n):
        if adj[seat]:
            seat1, seat2 = seat, adj[seat].pop()
            while seat2 != seat:
                result += 1
                adj[seat2].remove(seat1)
                seat1, seat2 = seat2, adj[seat2].pop()
    
    return result

expected = 2
actual = minimumSwapsCouples([1,3,4,0,2,5])
print actual == expected

expected = 0
actual = minimumSwapsCouples([3,2,0,1])
print actual == expected

# expected = 5
# actual = minimumSwapsCouples([3,30,50,90,16,91,65,18,61,58])
# print actual == expected

# expected = 2
# actual = minimumSwapsCouples([3,1,5,4,6,2])
# print actual == expected

# expected = 20
# actual = minimumSwapsCouples([55,37,19,46,66,32,07,81,33,76,00,28,92,26,99,06,56,29,17,52,90,79,91,83,12,40,82,84,02,21,11,68,98,34,73,10,57,58,64,36])
# print actual == expected

expected = 0
actual = minimumSwapsCouples([1,0])
print actual == expected

# expected = 37
# actual = minimumSwapsCouples([50,23,76,19,16,70,35,68,41,49,99,71,59,95,89,33,22,0,7,54,83,24,0,18,64,11,14,77,26,42,21,82,1,97,52,65,79,37,62,60,91,98,4,88,36,51,20,85,90,29,84,93,13,80,6,55,48,2,40,46,81,30,3,94,38,27,31,53,86,32,96,8,58,73,5])
# print actual == expected
