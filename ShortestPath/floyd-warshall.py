def floydWarshall(graph, distance, n):
    for i in range(1, n + 1):
        distance[i][i] = 0
    for i, edges in enumerate(graph):
        origin = i + 1
        for dest, weight in edges:
            distance[origin][dest] = min(weight, distance[origin][dest])

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                distance[i][j] = min(
                    distance[i][j], distance[i][k] + distance[k][j])


if __name__ == "__main__":
    graph = [
        [(2, 4), (4, 6)],  # vertex 1
        [(1, 3), (3, 7)],  # vertex 2
        [(1, 5), (4, 4)],  # vertex 3
        [(3, 2)]  # vertex 4
    ]
    graph = [
        [(2, 1), (4, 1)],
        [(3, 1)],
        [],
        [(3, 1)]
    ]
    distance = [[float('inf')] * (len(graph) + 1)
                for _ in range(len(graph) + 1)]
    floydWarshall(graph, distance, len(graph))

    for i in range(1, len(distance)):
        print(distance[i][1:])
