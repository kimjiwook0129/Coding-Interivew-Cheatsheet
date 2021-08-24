# https://www.acmicpc.net/problem/3665

from collections import deque


def topology_sort(graph, indegree, n):
    q = deque()
    result = []
    for idx in range(1, n + 1):
        if indegree[idx] == 0:
            q.append(idx)
    for i in range(1, n + 1):
        if len(q) == 0:
            print("IMPOSSIBLE")
            return
        if len(q) >= 2:
            print("?")
            return
        cur = q.popleft()
        result.append(cur)
        for i in range(1, n + 1):
            if graph[cur][i] == 1:
                indegree[i] -= 1
                if indegree[i] == 0:
                    q.append(i)
    for i in result[:-1]:
        print(i, end=" ")
    print(result[-1])


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        n = int(input())
        ranking = list(map(int, input().split()))
        m = int(input())
        conversions = []
        for _2 in range(m):
            conversions.append(tuple(list(map(int, input().split()))))
        graph = [[0] * (n + 1) for _ in range(n + 1)]
        indegree = [0] * (n + 1)
        for i, rank in enumerate(ranking):
            for rank2 in ranking[i + 1:]:
                graph[rank][rank2] = 1
                indegree[rank2] += 1
        for conversion in conversions:
            a, b = conversion
            graph[a][b] = 1 - graph[a][b]
            graph[b][a] = 1 - graph[b][a]
            if graph[a][b] == 1:
                indegree[a] -= 1
                indegree[b] += 1
            else:
                indegree[a] += 1
                indegree[b] -= 1
        topology_sort(graph, indegree, n)
