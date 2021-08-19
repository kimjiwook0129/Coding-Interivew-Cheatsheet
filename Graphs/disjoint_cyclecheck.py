
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
    sets = [[(1, 4), (2, 3), (2, 4), (5, 6)], [(1, 2), (2, 3), (1, 3)]]

    for _set in sets:
        v = max(list(map(max, _set)))
        e = len(_set)
        parent = [0] * (v + 1)
        for i in range(1, v + 1):
            parent[i] = i

        cycle = False
        for i in range(e):
            if find_parent(parent, _set[i][0]) == find_parent(parent, _set[i][1]):
                cycle = True
                break
            union_parent(parent, _set[i][0], _set[i][1])

        print("사이클 발생" if cycle else "사이클 없음")
