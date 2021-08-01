# Quicksort [퀵 정렬]
# Complexities : Time O(N log N) | Space O(N)
# Worst Time Complexity : O(N^2)


def quicksort(array, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        while left <= end and array[left] <= array[pivot]:
            left += 1
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]
    quicksort(array, start, right - 1)
    quicksort(array, right + 1, end)


def quicksort_python_simple(array):
    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:]

    left_side = [elem for elem in tail if elem <= pivot]
    right_side = [elem for elem in tail if elem > pivot]

    return quicksort_python_simple(left_side) + [pivot] + quicksort_python_simple(right_side)


if __name__ == "__main__":
    array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
    print(f"Initial Array : {array}")
    quicksort(array, 0, len(array) - 1)
    print(f"Final Sorted Array : {array}")
