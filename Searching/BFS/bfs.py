from collections import deque


def bfs(graph, start, visited):
    q = deque([start])
    visited[start] = True
    while q:
        cur = q.popleft()
        print(cur, end=" ")
        for i in graph[cur]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
    print()


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
    # 1 2 3 8 7 4 5 6
    bfs(graph, 1, visited)
