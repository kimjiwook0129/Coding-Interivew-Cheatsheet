'''
https://www.acmicpc.net/problem/18428

3 <= n <= 6
 
3 Obstacles Required
'''


def check_valid(n, table, teachers):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    for teacher in teachers:
        x, y = teacher
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            while nx >= 0 and ny >= 0 and nx < n and ny < n:
                if table[nx][ny] == 'O':
                    break
                if table[nx][ny] == 'S':
                    return False
                nx = nx + dx[i]
                ny = ny + dy[i]
    return True


def dfs(count, n, table, teachers):
    for i in range(n):
        for j in range(n):
            if table[i][j] == 'X':
                table[i][j] = 'O'
                count += 1
                if count == 3:
                    if check_valid(n, table, teachers):
                        return True
                else:
                    if dfs(count, n, table, teachers):
                        return True
                count -= 1
                table[i][j] = 'X'
    return False


if __name__ == "__main__":
    n = int(input())
    table = []
    teachers = []
    for i in range(n):
        data = list(input().split())
        for j in range(n):
            if data[j] == 'T':
                teachers.append((i, j))
        table.append(data)
    possible = dfs(0, n, table, teachers)
    if possible:
        print("YES")
    else:
        print("NO")
