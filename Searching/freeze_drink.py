# 이것이 코딩테스트다 p.149

def bfs(table, visited, row, col, N, M):
    drow = [1, -1, 0, 0]
    dcol = [0, 0, 1, -1]
    for i in range(4):
        nrow = row + drow[i]
        ncol = col + dcol[i]
        if nrow >= 0 and nrow < N and ncol >= 0 and ncol < M:
            if table[nrow][ncol] == 0 and not visited[nrow][ncol]:
                visited[nrow][ncol] = True
                bfs(table, visited, nrow, ncol, N, M)

if __name__ == "__main__":
    N, M = map(int, input().split())
    table, visited = [], []
    for _ in range(N):
        table.append(list(map(int, input())))
        visited.append([False for _ in range(M)])
    result = 0

    for i in range(N):
        for j in range(M):
            if table[i][j] == 0 and not visited[i][j]:
                visited[i][j] = True
                bfs(table, visited, i, j, N, M)
                result += 1

    print(result)
