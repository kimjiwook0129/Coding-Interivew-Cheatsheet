from collections import deque


def topology_sort(indegree, graph):
    result = []
    q = deque()

    for i in range(1, len(indegree)):
        if indegree[i] == 0:
            q.append(i)

    while q:
        cur = q.popleft()
        result.append(cur)
        for i in graph[cur]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    if len(result) != len(indegree) - 1:
        return "There is a cycle"
    return result


if __name__ == "__main__":
    directedGraph = [(1, 2), (1, 5), (2, 3), (2, 6),
                     (3, 4), (4, 7), (5, 6), (6, 4)]
    v, e = max(list(map(max, directedGraph))), len(directedGraph)

    indegree = [0] * (v + 1)
    graph = [[] for _ in range(v + 1)]

    for edge in directedGraph:
        a, b = edge
        graph[a].append(b)
        indegree[b] += 1

    result = topology_sort(indegree, graph)
    print(result)
