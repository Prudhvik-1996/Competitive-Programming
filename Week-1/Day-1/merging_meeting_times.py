from operator import itemgetter

def merge_ranges(meetings):
    if len(meetings) <= 1:
        return meetings

    meetings = sorted(meetings, key=itemgetter(0))
    pdl = [meetings[0]]
    meetings = meetings[1:]
    for (nstart, nend) in meetings:
        (start, end) = pdl[-1]
        if nstart <= end:
            if end <= nend:
                end = nend
            pdl[-1] = (start, end)
        else:
            pdl.append((nstart, nend))
    return pdl

# Tests

actual = merge_ranges([(1, 3), (2, 4)])
expected = [(1, 4)]
print(actual == expected)

actual = merge_ranges([(5, 6), (6, 8)])
expected = [(5, 8)]
print(actual == expected)

actual = merge_ranges([(1, 8), (2, 5)])
expected = [(1, 8)]
print(actual == expected)

actual = merge_ranges([(1, 3), (4, 8)])
expected = [(1, 3), (4, 8)]
print(actual == expected)

actual = merge_ranges([(1, 4), (2, 5), (5, 8)])
expected = [(1, 8)]
print(actual == expected)

actual = merge_ranges([(5, 8), (1, 4), (6, 8)])
expected = [(1, 4), (5, 8)]
print(actual == expected)

actual = merge_ranges([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)])
expected = [(0, 1), (3, 8), (9, 12)]
print(actual == expected)
