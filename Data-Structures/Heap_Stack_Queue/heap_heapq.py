import heapq

# Complexities : Time O(N log N) | Space O(N)


def heapsort(iterable, reverse=False):
    heap = []  # O(N)
    result = []  # O(N)
    order = -1 if reverse else 1
    for value in iterable:  # O(N)
        heapq.heappush(heap, order * value)  # O(log N)
    for _ in range(len(heap)):  # O(N)
        result.append(order * heapq.heappop(heap))  # O(log N)
    return result


if __name__ == '__main__':
    result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
    print(result)
    result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0], True)
    print(result)
