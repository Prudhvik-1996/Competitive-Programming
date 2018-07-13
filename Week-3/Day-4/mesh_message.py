def bfs_get_path(graph, start_node, end_node):

    # Find the shortest route in the network between the two users
    s = start_node
    d = end_node
    q = []
    
    count = 0
    for _ in graph:
        count += 1
    
    marked = {}
    edgeTo = {}
    distTo = {}
    
    for i in graph:
        marked[i] = False
        edgeTo[i] = 0
        distTo[i] = 100000
    
    marked[s] = True
    q.append(s)
    while q != []:
        v = q.pop(0)
        for w in graph[v]:
            if not marked[w]:
                edgeTo[w] = v
                marked[w] = True
                distTo[w] = distTo[v] + 1
                q.append(w)
    
    if not marked[d]:
        return None
    
    path = []
    x = d
    while x!=s:
        path.append(x)
        x = edgeTo[x]
    path.append(x)
    
    return path[::-1]

# Tests

graph = {
    'a': ['b', 'c', 'd'],
    'b': ['a', 'd'],
    'c': ['a', 'e'],
    'd': ['a', 'b'],
    'e': ['c'],
    'f': ['g'],
    'g': ['f'],
}

actual = bfs_get_path(graph, 'a', 'e')
expected = ['a', 'c', 'e']
print(actual == expected)

actual = bfs_get_path(graph, 'd', 'c')
expected = ['d', 'a', 'c']
print(actual == expected)

actual = bfs_get_path(graph, 'a', 'c')
expected = ['a', 'c']
print(actual == expected)

actual = bfs_get_path(graph, 'f', 'g')
expected = ['f', 'g']
print(actual == expected)

actual = bfs_get_path(graph, 'g', 'f')
expected = ['g', 'f']
print(actual == expected)

actual = bfs_get_path(graph, 'a', 'a')
expected = ['a']
print(actual == expected)

actual = bfs_get_path(graph, 'a', 'f')
expected = None
print(actual == expected)