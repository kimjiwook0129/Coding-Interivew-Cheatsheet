

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
    G, P = int(input()), int(input())
    result = 0
    parent = [0] * (G + 1)
    for i in range(1, G + 1):
        parent[i] = i
    for i in range(1, P + 1):
        max_gate = find_parent(parent, int(input()))
        if max_gate == 0:
            break
        union_parent(parent, max_gate, max_gate - 1)
        result += 1
    print(result)
