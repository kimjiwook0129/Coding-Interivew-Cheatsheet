## Graphs [그래프]

### Disjoint Sets [서로소 집합]

- Sets without having a common element [공통 원소가 없는 집합들]
- Used for processing data separated into multiple disjoint sets [서로소 집합들로 나뉘어진 데이터 처리를 위해 사용]
- Concept [원리]:
  - Use union operation to check whether two nodes are connected [union 연산으로 서로 연결된 두 노드를 확인]
    - Find the root nodes of the two nodes [두 노드의 부모 노드들 찾기]
    - Set the root node to be the child of another root node [한 부모 노드가 다른 부모 노드의 child 노드가 되도록 설정]
  - Repeat the first process for all the given union operations [모든 union 연산이 끝날때 까지 1번 작업 반복]
- Complexities : Time O(U + F log U) where U: # of union op, F: # of find op | Space O(V)

### Kruskal Algorithms [크루스칼 알고리즘]

- To find the minimum spanning tree for a connected weighted graph. [가중치가 있는 연결 그래프에서 최소 신장 트리를 찾기 위해 사용한다.]
- It is classified as a greedy algorithm. [그리디 알고리즘으로 분류된다.]
- Concept [원리]:
  - Sort the edges in the weight ascending order [간선을 비용에 따라 오름차순으로 정렬]
  - Check whether the current edge causes a cycle [현재 간선이 사이클을 발생시키는지 확인]
    - If cycle does not occur, add it in our minimum spanning tree [사이클 발생하지 않을 시, 최소 신장 트리에 포함]
    - If cycle does occur, do not include it [사이클 발생 시, 포함하지 말 것]
  - Repeat the 2nd step for all the edges [모든 간선에 대하여 2번째 과정을 반복]
- Complexities : Time O(E log E) | Space O(V + E)

### Topology Sort [위상 정렬]

- To linearly order the vertices such that for every directed edge uv from vertex u to v, u comes before v in the order [방향 그래프의 노드를 방향성에 거스르지 않도록 순서대로 나열하는 것]
- It is classified as a sorting algorithm. [정렬 알고리즘으로 분류된다.]
- Complexities : Time O(V + E) | Space O(V + E)
- Concept [원리]:
  - Insert a node with degree 0 into the queue [진입차수가 0인 노드를 큐에 삽입]
  - Repeat the process below until the queue is empty [큐가 빌 때까지 다음 과정 반복]
    - Remove edges starting from the popped node from the queue [큐에서 나온 노드에서 출발하는 간선을 그래프에서 제거]
    - Insert node with a degree 0 into the queue [진입차수가 0이 된 노드를 큐에 삽입]
