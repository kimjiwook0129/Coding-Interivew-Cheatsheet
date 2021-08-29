# https://www.acmicpc.net/problem/19237

# 1, 2, 3, 4 => 위, 아래, 왼쪽, 오른쪽

drow = [0, -1, 1, 0, 0]
dcol = [0, 0, 0, -1, 1]


def updateSmell(sharksState, smellTable, k):
    for i in range(N):
        for j in range(N):
            if smellTable[i][j]['smell'] > 0:
                smellTable[i][j]['remain'] -= 1
                if smellTable[i][j]['remain'] == 0:
                    smellTable[i][j]['smell'] = 0
    for shark, state in sharksState.items():
        row, col, dir = state
        smellTable[row][col]['smell'] = shark
        smellTable[row][col]['remain'] = k


def deleteAnyDuplicateStates(sharksState):
    lst = []
    for shark, state in sharksState.items():
        lst.append([shark, state[0], state[1], state[2]])
    lst.sort(key=lambda x: x[1])
    i = 0
    while i + 1 < len(lst):
        if lst[i][1] == lst[i + 1][1] and lst[i][2] == lst[i + 1][2]:
            if lst[i][0] > lst[i + 1][0]:
                del sharksState[lst[i][0]]
                del lst[i]
            else:
                del sharksState[lst[i + 1][0]]
                del lst[i + 1]
        else:
            i += 1


def nextCells(smellTable, sharksState, N):
    dirs = {}
    for shark, state in sharksState.items():
        dirs[shark] = []
        for i in range(1, 5):
            nrow = state[0] + drow[i]
            ncol = state[1] + dcol[i]
            if nrow >= 0 and nrow < N and ncol >= 0 and ncol < N:
                if smellTable[nrow][ncol]["smell"] == 0:
                    dirs[shark].append((nrow, ncol, i))
        if len(dirs[shark]) > 0:
            continue
        for i in range(1, 5):
            nrow = state[0] + drow[i]
            ncol = state[1] + dcol[i]
            if nrow >= 0 and nrow < N and ncol >= 0 and ncol < N:
                if smellTable[nrow][ncol]["smell"] == shark:
                    dirs[shark].append((nrow, ncol, i))
    return dirs


def updateTable(smellTable, sharksState, sharksPriority, N, k):
    possibleMoves = nextCells(smellTable, sharksState, N)
    for shark in possibleMoves.keys():
        curDir = sharksState[shark][2]
        priority4 = sharksPriority[shark][curDir]
        updated = False
        for _dir in priority4:
            for move in possibleMoves[shark]:
                if move[2] == _dir:
                    sharksState[shark] = [move[0], move[1], move[2]]
                    updated = True
                if updated:
                    break
            if updated:
                break
    deleteAnyDuplicateStates(sharksState)
    updateSmell(sharksState, smellTable, k)
    if len(sharksState.keys()) == 1:
        return True
    return False


if __name__ == "__main__":
    N, M, k = map(int, input().split())
    smellTable = [[{"smell": 0, "remain": 0}
                   for _ in range(N)] for __ in range(N)]
    sharksState = {}
    sharksPriority = [
        [[0 for _ in range(5)] for __ in range(5)] for ___ in range(M + 1)]
    # 1, 2, 3, 4 : 위, 아래, 왼쪽, 오른쪽
    for i in range(N):
        data = list(map(int, input().split()))
        for j in range(N):
            cellVal = data[j]
            if cellVal > 0:  # It is a shark
                sharksState[cellVal] = [i, j, 0]  # [row, col, dir]
                smellTable[i][j]["smell"] = cellVal
                smellTable[i][j]["remain"] = k
    sharkDirections = list(map(int, input().split()))
    for idx, shark_dir in enumerate(sharkDirections):
        sharksState[idx + 1][2] = shark_dir
    for shark_num in range(1, M + 1):
        for dir_num in range(1, 5):
            data = list(map(int, input().split()))
            for idx, each_dir in enumerate(data):
                sharksPriority[shark_num][dir_num][idx + 1] = each_dir
    timeTaken = 0
    while timeTaken < 1000:
        onlyOneRemaining = updateTable(
            smellTable, sharksState, sharksPriority, N, k)
        timeTaken += 1
        if onlyOneRemaining:
            break

    print(-1 if timeTaken >= 1000 else timeTaken)
