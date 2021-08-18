# https://www.acmicpc.net/problem/1932

n = int(input())
table = []
table.append([int(input())])
for i in range(1, n):
    table.append(list(map(int, input().split())))
    for j, e in enumerate(table[i]):
        best = 0
        if j > 0:
            best = table[i - 1][j - 1]
        if j < len(table[i]) - 1:
            best = max(best, table[i - 1][j])
        table[i][j] = e + best
print(max(table[n - 1]))
