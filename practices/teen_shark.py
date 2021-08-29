# https://www.acmicpc.net/problem/19236

from collections import deque
import copy

drow = [0, -1, -1, 0, 1, 1, 1, 0, -1]
dcol = [0, 0, -1, -1, -1, 0, 1, 1, 1]


def updateTable(table, sharkRow, sharkCol):
    smallestFish = float('inf')
    fishRow, fishCol = 0, 0
    biggestFish = 0
    for i in range(4):
        for j in range(4):
            curFish = table[i][j][0]
            biggestFish = max(biggestFish, curFish)
            if curFish > 0 and smallestFish > curFish:
                smallestFish = curFish
                fishRow, fishCol = i, j
    while True:

        while True:
            curDir = table[fishRow][fishCol][1]
            nrow, ncol = fishRow + drow[curDir], fishCol + dcol[curDir]
            if nrow >= 0 and nrow < 4 and ncol >= 0 and ncol < 4:
                if not (nrow == sharkRow and ncol == sharkCol):
                    table[nrow][ncol][0], table[fishRow][fishCol][0] = table[fishRow][fishCol][0], table[nrow][ncol][0]
                    table[nrow][ncol][1], table[fishRow][fishCol][1] = table[fishRow][fishCol][1], table[nrow][ncol][1]
                    break
            curDir = 1 if curDir == 8 else curDir + 1
            table[fishRow][fishCol][1] = curDir

        if smallestFish == biggestFish:
            return
        nextSmallestFish = float('inf')
        nextSmallRow, nextSmallCol = 0, 0
        for i in range(4):
            for j in range(4):
                curFish = table[i][j][0]
                if curFish > smallestFish and nextSmallestFish > curFish:
                    nextSmallestFish = curFish
                    nextSmallRow, nextSmallCol = i, j
        smallestFish = nextSmallestFish
        fishRow, fishCol = nextSmallRow, nextSmallCol


if __name__ == "__main__":
    table = []
    for _ in range(4):
        data = list(map(int, input().split()))
        row = []
        for i in range(0, len(data), 2):
            row.append([data[i], data[i + 1]])
        table.append(row)
    result = table[0][0][0]
    table[0][0][0] = 0
    updateTable(table, 0, 0)
    q = deque([(0, 0, result, table)])
    while q:
        row, col, curResult, curTable = q.popleft()
        result = max(result, curResult)
        dir = curTable[row][col][1]
        nrows, ncols = [], []
        for i in range(1, 4):
            nrows.append(row + i * drow[dir])
            ncols.append(col + i * dcol[dir])
        for i in range(3):
            nrow, ncol = nrows[i], ncols[i]
            if nrow >= 0 and nrow < 4 and ncol >= 0 and ncol < 4:
                if curTable[nrow][ncol][0] > 0:
                    copyTable = copy.deepcopy(curTable)
                    q.append((nrow, ncol, curResult +
                             copyTable[nrow][ncol][0], copyTable))
                    copyTable[nrow][ncol][0] = 0
                    updateTable(copyTable, nrow, ncol)
    print(result)

# 7 6 2 3 15 6 9 8
# 3 1 1 8 14 7 10 1
# 6 1 13 6 4 3 11 4
# 16 1 8 7 5 2 12 2
# 33

# 16 7 1 4 4 3 12 8
# 14 7 7 6 3 4 10 2
# 5 2 15 2 8 3 6 4
# 11 8 2 4 13 5 9 4
# 43

# 12 6 14 5 4 5 6 7
# 15 1 11 7 3 7 7 5
# 10 3 8 3 16 6 1 1
# 5 8 2 7 13 6 9 2
# 76
