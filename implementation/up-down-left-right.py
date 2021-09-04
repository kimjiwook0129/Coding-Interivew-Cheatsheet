# 이것이 코딩테스트다 p.110
if __name__ == "__main__":
    N = int(input())
    orders = list(input().split())
    row, col = 1, 1
    drow = [0, 0, -1, 1]
    dcol = [-1, 1, 0, 0]
    direction = {'L': 0, 'R': 1, 'U': 2, 'D': 3}
    for order in orders:
        nrow = row + drow[direction[order]]
        ncol = col + dcol[direction[order]]
        if nrow > 0 and nrow <= N and ncol > 0 and ncol <= N:
            row, col = nrow, ncol
    print(row, col)
