# https://programmers.co.kr/learn/courses/30/lessons/60063
# Moving on the Blocks

from collections import deque


def get_next_pos(pos, board, n):
    positions = []
    pos1, pos2 = pos
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    for i in range(4):
        nx1, nx2 = pos1[0] + dx[i], pos2[0] + dx[i]
        ny1, ny2 = pos1[1] + dy[i], pos2[1] + dy[i]
        if nx1 >= 0 and nx2 >= 0 and ny1 >= 0 and ny2 >= 0 \
                and nx1 < n and nx2 < n and ny1 < n and ny2 < n:
            if board[nx1][ny1] == 0 and board[nx2][ny2] == 0:
                positions.append({(nx1, ny1), (nx2, ny2)})
    if pos1[0] == pos2[0]:  # horizontal
        for i in [-1, 1]:
            x = pos1[0] + i
            if not (x >= 0 and x < n):
                continue
            if board[x][pos1[1]] == 0 and board[x][pos2[1]] == 0:
                positions.append({pos1, (x, pos1[1])})
                positions.append({(x, pos2[1]), pos2})
    else:  # vertical
        for j in [-1, 1]:
            y = pos1[1] + j
            if not (y >= 0 and y < n):
                continue
            if board[pos1[0]][y] == 0 and board[pos2[0]][y] == 0:
                positions.append({pos1, (pos1[0], y)})
                positions.append({pos2, (pos2[0], y)})
    return positions


def solution(board):
    n = len(board)
    q = deque()
    visited = []
    pos = {(0, 0), (0, 1)}
    q.append((pos, 0))
    visited.append(pos)
    while q:
        pos, cost = q.popleft()
        if (n - 1, n - 1) in pos:
            return cost
        for next_pos in get_next_pos(pos, board, n):
            if next_pos not in visited:
                q.append((next_pos, cost + 1))
                visited.append(next_pos)
    return 0


if __name__ == "__main__":
    n = int(input())
    matrix = []
    for _ in range(n):
        data = list(map(int, input().split()))
        matrix.append(data)
    result = solution(matrix)
    print(result)
