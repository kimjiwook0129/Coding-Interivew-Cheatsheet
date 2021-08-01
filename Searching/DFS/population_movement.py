'''
https://www.acmicpc.net/problem/16234

N, L, R (1 <= N <= 50, 1 <= L <= R <= 100)
0 <= A[r][c] <= 100
인구 이동 횟수는 2,000회보다 작거나 같다
'''
from collections import deque


def bfs(i, j, N, L, R, table, visited):
    areas = []
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    q = deque([(i, j)])
    while q:
        x, y = q.popleft()
        if visited[x][y]:
            continue
        visited[x][y] = True
        areas.append((x, y))
        for idx in range(4):
            nx = x + dx[idx]
            ny = y + dy[idx]
            if nx >= 0 and nx < N and ny >= 0 and ny < N:
                if visited[nx][ny]:
                    continue
                difference = abs(table[x][y] - table[nx][ny])
                if difference >= L and difference <= R:
                    q.append((nx, ny))
    return areas


def population_update(areas, table):
    population = 0
    length = len(areas)
    for (x, y) in areas:
        population += table[x][y]
    for (x, y) in areas:
        table[x][y] = population // length


if __name__ == "__main__":
    N, L, R = map(int, input().split())
    table = []
    for i in range(N):
        table.append(list(map(int, input().split())))
    day = 0
    while True:
        visited = [[False] * N for _ in range(N)]
        change = False
        for i in range(N):
            for j in range(N):
                if visited[i][j]:
                    continue
                areas = bfs(i, j, N, L, R, table, visited)
                if len(areas) > 1:
                    population_update(areas, table)
                    change = True
        if not change:
            break
        day += 1
    print(day)
