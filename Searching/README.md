## Searching [탐색]

### BFS(Breath First Search) [넓이 우선 탐색]

- Searches up the nearest nodes first [가장 가까운 노드부터 탐색한다]
- Concept [원리]:
  - Insert the start node to the queue and update as visited [시작 노드를 큐에 넣고 방문 처리]
  - Pop the node out of the queue update as visited, then insert its neighbours to the queue (if already visited, don't insert it) [큐에 들어있는 노드를 꺼내 주변 노드들을 큐에 넣고 방문처리 (이미 방문 처리가 되어있을시 무시)]
  - Repeat the second step until the queue is empty[큐가 빌 때까지 2번째 절차 반복]

### DFS(Depth First Search) [깊이 우선 탐색]

- Searches up the deepest part of the graph first [그래프에서 가장 깊은 부분부터 탐색]
- Concept [원리]:
  - Insert the start node to the stack and update as visited [시작 노드를 스택에 넣고 방문 처리]
  - Insert the top node's neighbours to the stack if they are not visited [상단 노드의 인접 노드들이 아직 방문 전이면 스택에 삽입한다]
  - If the top node's neighbours are all visited, pop the top node [상단 노드의 인접 노드들이 모두 방문 처리가 되었을시 상단 노드를 꺼낸다]
  - Repeat the second & third step until the queue is empty[큐가 빌 때까지 2, 3번째 절차 반복]

### BS(Binary Search) [이진 탐색]

- Can only be used when the array is sorted [배열이 정렬되어 있을 때만 사용 가능]
- Search by bisecting the search area [탐색 범위를 반으로 쪼개며 나아가는 탐색 방법]
