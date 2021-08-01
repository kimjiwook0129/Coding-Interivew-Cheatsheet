## Sorting [정렬]

### Selection Sort [선택 정렬]

- Complexities : Time O(N^2) | Space O(N)
- The algorithm swaps the smallest the most front, and then swaps the next smallest and the second most front, and so on.
- Most primitive sorting algorithm, easy to implement but inefficient.

### Insertion Sort [삽입 정렬]

- Complexities : Time O(N^2) | Space O(N)
- Best Time Complexity : O(N)
- The algorithm checks the element one by one and inserts each point to its appropriate index.
- While running, the sorted subarray at the front is always sorted.
- If the given array is almost sorted already, then it acts as almost O(N).

### Quick Sort [퀵 정렬]

- Complexities : Time O(N log N) | Space O(N)
- One of the most commonly used sorting algorithm.
- The algorithm sets up a pivot point and swaps the locations of bigger and smaller elements compared to the pivot element.
- There are multiple ways of paritioning methods, the most commonly used is the 'hoare partition'.

### Count Sort [계수 정렬]

- Complexities : Time O(N + K) | Space O(N + K)

### Merge Sort [합병 정렬]

- Complexities : Time O(N log N) | Space O(N)
