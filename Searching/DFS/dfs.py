def dfs(graph, start, visited):
    print(start, end=" ")
    visited[start] = True
    for i in graph[start]:
        if not visited[i]:
            dfs(graph, i, visited)


if __name__ == "__main__":
    graph = [
        [],
        [2, 3, 8],
        [1, 7],
        [1, 4, 5],
        [3, 5],
        [3, 4],
        [7],
        [2, 6, 8],
        [1, 7]
    ]
    visited = [False] * len(graph)
    # 1 2 7 6 8 3 4 5
    dfs(graph, 1, visited)
    print()
