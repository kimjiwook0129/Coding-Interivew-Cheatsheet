
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
    unions = [(1, 4), (2, 3), (2, 4), (5, 6)]
    vertex, edge = 6, len(unions)
    parent = [0] * (vertex + 1)
    for i in range(1, vertex + 1):
        parent[i] = i

    for i in range(edge):
        union_parent(parent, unions[i][0], unions[i][1])
    for i in range(1, vertex + 1):
        find_parent(parent, i)
    print("Where each node belongs to (parent):")
    print(f'{"Nodes: ":>{15}}', end="")
    for i in range(1, vertex + 1):
        print(i, end=" ")
    print()
    print(f'{"Parents: ":>{15}}', end="")
    for i in range(1, vertex + 1):
        print(parent[i], end=" ")
    print()
