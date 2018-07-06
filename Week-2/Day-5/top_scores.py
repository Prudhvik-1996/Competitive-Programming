def sort_scores(unsorted_scores, highest_possible_score):
    l = [0]*(highest_possible_score+1)
    for i in unsorted_scores:
        l[i] += 1
    res = []
    for i in range(len(l)-1,-1,-1):
        if l[i] != 0:
            temp = [i]*l[i]
            res.extend(temp)
    return res

# Tests

actual = sort_scores([], 100)
expected = []
print(actual == expected)

actual = sort_scores([55], 100)
expected = [55]
print(actual == expected)

actual = sort_scores([30, 60], 100)
expected = [60, 30]
print(actual == expected)

actual = sort_scores([37, 89, 41, 65, 91, 53], 100)
expected = [91, 89, 65, 53, 41, 37]
print(actual == expected)