import heapq

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]


def dijkstra(graph, distance):
    q = [(0, 1, 1)]  # (Weight, row, col)
    distance[1][1] = 0
    while q:
        weight, row, col = heapq.heappop(q)
        if distance[row][col] < weight:
            continue  # Already visited
        for i in graph[row][col]:
            cost = weight + i[0]
            if cost < distance[i[1]][i[2]]:
                distance[i[1]][i[2]] = cost
                heapq.heappush(q, (cost, i[1], i[2]))


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N = int(input())
        distance = [[float('inf')] * (N + 1) for _ in range(N + 1)]
        graph = [[[] for _ in range(N + 1)] for _ in range(N + 1)]
        rawGraph = [[]]
        for _ in range(N):
            rawGraph.append([float('inf')] + list(map(int, input().split())))
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if nx >= 1 and ny >= 1 and nx <= N and ny <= N:
                        graph[i][j].append((rawGraph[nx][ny], nx, ny))
        dijkstra(graph, distance)
        print(distance[N][N] + rawGraph[1][1])
