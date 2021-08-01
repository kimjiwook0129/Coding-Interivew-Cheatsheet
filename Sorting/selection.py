# Selection Sort [선택 정렬]
# Complexities : Time O(N^2) | Space O(N)


def selection_sort(array, printEach=True):
    for i in range(len(array)):
        min_index = i
        for j in range(i + 1, len(array)):
            if array[min_index] > array[j]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
        if printEach:
            print(array)


if __name__ == "__main__":
    array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
    print(f"Initial Array : {array}")
    selection_sort(array)
    print(f"Final Sorted Array : {array}")
