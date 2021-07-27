## Heap / Stack / Queue [힙 / 스택 / 큐]

|    Data Structure [자료구조] | Data Extracted [추출되는 데이터]                  |
| ---------------------------: | :------------------------------------------------ |
|                 Stack [스택] | LIFO [가장 나중에 삽입된 데이터]                  |
|                   Queue [큐] | FIFO [가장 먼저 삽입된 데이터]                    |
| Priority Queue [우선순위 큐] | With Highest Priority [가장 우선순위 높은 데이터] |

### Heap [힙]

Heap is mostly used for implementing a Priority Queue. [힙은 대개 우선순위 큐를 구현하는데 사용한다.]

파이썬에서는 우선순위 큐로 PriorityQueue 혹은 heapq를 사용할 수 있다.
heapq가 더 빠르게 동작하기 때문에 heapq를 추천한다.

파이썬/Java에서는 기본적으로 최소 힙 구조를 사용한다.
C++에서는 최대힙이 기본이다.

| 우선순위 큐 구현 방식 | 삽입 시간 | 삭제 시간 |
| --------------------: | --------- | --------- |
|                리스트 | O(1)      | O(N)      |
|              힙(Heap) | O(logN)   | O(logN)   |

```python
import heapq
heapq.heappush(heapQueue, value)
heapq.heappop(heapQueue)
```
