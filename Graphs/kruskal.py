def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


if __name__ == "__main__":
    graph = [(1, 2, 29), (1, 5, 75), (2, 3, 35), (2, 6, 34),
             (3, 4, 7), (4, 6, 23), (4, 7, 13), (5, 6, 53), (6, 7, 25)]
    v, e = max(list(map(max, graph))), len(graph)

    graph.sort(key=lambda x: x[2])

    parent = [0] * (v + 1)
    for i in range(1, v + 1):
        parent[i] = i
    minSpanWeight = 0
    for edge in graph:
        a, b, w = edge
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            minSpanWeight += w
    print(minSpanWeight)
