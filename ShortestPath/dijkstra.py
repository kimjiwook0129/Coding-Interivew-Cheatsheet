import heapq


def dijkstra(start, graph, distance):
    q = [(0, start)]
    distance[start] = 0
    while q:
        dist, node = heapq.heappop(q)
        if distance[node] < dist:
            continue
        for i in graph[node]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


if __name__ == "__main__":
    start = 1  # starting at vertex 1
    graph = [
        [],  # Just empty
        [(2, 2), (3, 5), (4, 1)],  # vertex 1
        [(3, 3), (4, 2)],  # vertex 2
        [(2, 3), (6, 5)],  # vertex 3
        [(3, 3), (5, 1)],  # vertex 4
        [(3, 1), (6, 2)],  # vertex 5
        []  # vertex 6
    ]
    distance = [float('inf')] * (len(graph) + 1)
    dijkstra(start, graph, distance)

    print(f"The distances from vertex {start} to:")
    for i in range(1, len(graph)):
        dis = distance[i] if distance[i] < float('inf') else "Not Reachable"
        print(f"To vertex {i} : {dis}")
