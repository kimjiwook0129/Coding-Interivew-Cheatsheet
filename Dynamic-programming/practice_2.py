# https://www.acmicpc.net/problem/14501

N = int(input())
table = [[]]
for _ in range(N):
    table.append(list(map(int, input().split())))
for day in range(N, 0, -1):
    dayNeed, moneyGet = table[day]
    endDay = day + dayNeed - 1
    nextDay = 0 if day + 1 > N else table[day + 1][1]
    if endDay <= N:  # Works
        doneDay = 0 if endDay + 1 > N else table[endDay + 1][1]
        table[day][1] = max(table[day][1] + doneDay, nextDay)
    else:
        table[day][1] = nextDay
print(table[1][1])
