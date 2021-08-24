# https://www.acmicpc.net/problem/2887

def find_parent(parents, x):
    if parents[x] != x:
        parents[x] = find_parent(parents, parents[x])
    return parents[x]


def union_parent(parents, a, b):
    a = find_parent(parents, a)
    b = find_parent(parents, b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b


N = int(input())
x, y, z = [], [], []
for i in range(1, N + 1):
    data = list(map(int, input().split()))
    x.append((i, data[0]))
    y.append((i, data[1]))
    z.append((i, data[2]))
x.sort(key=lambda a: a[1])
y.sort(key=lambda a: a[1])
z.sort(key=lambda a: a[1])
edges = []
for i in range(N - 1):
    edges.append((x[i][0], x[i + 1][0], x[i + 1][1] - x[i][1]))
    edges.append((y[i][0], y[i + 1][0], y[i + 1][1] - y[i][1]))
    edges.append((z[i][0], z[i + 1][0], z[i + 1][1] - z[i][1]))
parents = [0] * (N + 1)
for i in range(1, N + 1):
    parents[i] = i
edges.sort(key=lambda x: x[2])
total = 0
for edge in edges:
    a, b, weight = edge
    if find_parent(parents, a) != find_parent(parents, b):
        union_parent(parents, a, b)
        total += weight
print(total)
