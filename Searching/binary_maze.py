# 이것이 코딩테스트다 p.152

# Sample Input:
# 5 6
# 101010
# 111111
# 000001
# 111111
# 111111
# Output : 10

from collections import deque

# Complexities : Time O(NM) | Space O(NM)

if __name__ == "__main__":
    N, M = map(int, input().split())
    maze = []
    for _ in range(N):
        maze.append(list(map(int, input())))
    q = deque([(0, 0, 1)])
    run = True
    while q and run:
        row, col, move = q.popleft()
        drow = [0, 0, -1, 1]
        dcol = [1, -1, 0, 0]
        for i in range(4):
            nrow, ncol = row + drow[i], col + dcol[i]
            if nrow >= 0 and nrow < N and ncol >= 0 and ncol < M:
                if nrow == N - 1 and ncol ==  M - 1:
                    print(move + 1)
                    run = False
                    break
                if maze[nrow][ncol] == 0: continue
                if maze[nrow][ncol] == 1:
                    q.append((nrow, ncol, move + 1))
                    maze[nrow][ncol] = -1

