# 이것이 코딩테스트다 p.118

if __name__ == "__main__":
    # (A, B) -> A는 북쪽으로부터 떨어진, B는 서쪽으로부터 떨어진
    # 1.왼쪽 방향부터 차례대로 갈 곳 정한다
    # 2.왼쪽에 아직 가보지 않은 칸 존재 시, 왼쪽 회전 후 왼쪽으로 한 칸 전진, 가보지 않은 칸이 없다면 왼쪽으로ㅎ 회전만 하고 1단계로
    # 3.만약 네 방향 모두 가본 or 바다일 경우 바로보는 방향 유지 한 칸으로 뒤로 간다- >1 단계로 이때 뒤쪽이 바다이면 게임 끝
    # 3 < = N, M <= 50
    # 0, 1, 2, 3 -> 북 동 남 서
    # 0, 1 육 바
    # 0 > 3 > 2 > 1 > 0 (방향 전환)
    N, M = map(int, input().split())
    row, col, direction = map(int, input().split())
    row, col = row, col
    table = []
    visited = []
    for _ in range(N):
        table.append(list(map(int, input().split())))
        visited.append([False for _ in range(M)])
    visited[row][col] = True
    drow = [-1, 0, 1, 0]
    dcol = [0, 1, 0, -1]
    dir_try = 0
    result = 1
    while True:
        # step 1
        direction = direction - 1 if direction > 0 else 3
        nrow, ncol = row + drow[direction], col + dcol[direction]
        # step 2
        if nrow >= 0 and nrow < N and ncol >= 0 and ncol < M:
            if table[nrow][ncol] == 0 and not visited[nrow][ncol]:
                row, col = nrow, ncol
                visited[row][col] = True
                result += 1
                dir_try = 0
                continue
        dir_try += 1
        if dir_try < 4: continue
        dir_try = 0
        # step 3
        tempDir = direction
        if direction >= 2: tempDir -= 2
        else: tempDir += 2
        nrow, ncol = row + drow[tempDir], col + dcol[tempDir]
        if nrow >= 0 and nrow < N and ncol >= 0 and ncol < M:
            if table[nrow][ncol] == 1:
                break
            row, col = nrow, ncol
            continue
        break
    print(result)