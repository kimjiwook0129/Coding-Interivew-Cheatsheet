## Shortest Path [최단 경로 알고리즘]

### Dijkstra's Algorithm [다익스트라 알고리즘]

Dijkstra's algorithm helps find the shortest pathes from a node to node in the given graph.
Dijkstra's algorithm requires any edge of the graph to not have negative weight. [다익스트라 알고리즘은 주어진 그래프 내 한 노드에서 다른 노드로 가는 최단 경로를 구해주는 알고리즘이다. 다익스트라 알고리즘은 음의 간선이 없을 때만 작동한다.]

- It is classified as a greedy algorithm. [그리디 알고리즘으로 분류된다.]
- Concept [원리]:
  - Set the initial node
  - Initialize the shortest path table
  - Choose a node with the shortest path among the ones not visited
  - Update the shortest path table
  - Repeat the 3rd & 4th steps
- Complexities : Time O(E log V) | Space O(V + E)

### Floyd-Warshall Algorithm [플로이드 워셜 알고리즘]

Floyd-Warshall Algorithm is used when we need to find the shortest pathes from all the nodes to all the nodes. [플로이드 워셜 알고리즘은 모든 노드에서 다른 모든 노드로의 최단 경로를 모두 구해야 할때 사용한다.]

- It is classified as a dynamic programming algorithm. [다이나믹 프로그래밍으로 분류된다.]
- Complexities : Time O(N<sup>3</sup>) | Space O(N<sup>2</sup>)
- Concept [원리]:
  - Set the distance matrix (# of vertex, # of vertex)
  - Set the distance to 0 for where the origin and destination are equal (same vertex)
  - Update the distance matrix using the graph given
  - Update the distance whenever the distance via another node is shorter (D<sub>ab</sub> = min(D<sub>ab</sub>, D<sub>ak</sub> + D<sub>kb</sub>))
