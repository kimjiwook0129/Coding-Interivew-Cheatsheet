# https://www.acmicpc.net/problem/16236

from collections import deque


def bfs(table, curRow, curCol, N, sharkSize):
    visited = [[False] * N for _ in range(N)]
    q = deque([(0, curRow, curCol)])
    dx, dy = [-1, 0, 0, 1], [0, -1, 1, 0]
    arrayOfPossibilities = []
    while q:
        dis, row, col = q.popleft()
        visited[row][col] = True
        if len(arrayOfPossibilities) > 0 and dis > arrayOfPossibilities[0][2]:
            break
        if table[row][col] > 0 and table[row][col] < sharkSize:
            arrayOfPossibilities.append((row, col, dis))

        for i in range(4):
            nx = row + dx[i]
            ny = col + dy[i]
            if nx >= 0 and nx < N and ny >= 0 and ny < N:
                if not visited[nx][ny]:
                    if table[nx][ny] <= sharkSize:
                        q.append((dis + 1, nx, ny))
                    else:
                        visited[nx][ny] = True
    if len(arrayOfPossibilities) > 0:
        arrayOfPossibilities.sort()
        thisOne = arrayOfPossibilities[0]
        return ((thisOne[0], thisOne[1]), thisOne[2])
    return ((1, 1), -1)


if __name__ == "__main__":
    N = int(input())
    table = []
    curRow, curCol = 0, 0
    for i in range(N):
        data = list(map(int, input().split()))
        if 9 in data:
            j = data.index(9)
            curRow, curCol = i, j
        table.append(data)
    sharkSize, sharkFeed = 2, 0

    time = 0
    while True:
        nextCoord, distance = bfs(table, curRow, curCol, N, sharkSize)
        if distance == -1:
            break
        time += distance
        table[curRow][curCol] = 0
        curRow, curCol = nextCoord
        table[curRow][curCol] = 9
        sharkFeed += 1
        if sharkFeed == sharkSize:
            sharkSize += 1
            sharkFeed = 0
    print(time)
