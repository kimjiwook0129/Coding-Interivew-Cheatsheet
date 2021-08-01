# Insertion Sort [삽입 정렬]
# Complexities : Time O(N^2) | Space O(N)
# Best Time Complexity : O(N)


def insertion_sort(array, printEach=True):
    for i in range(1, len(array)):
        for j in range(i, 0, -1):
            if array[j] < array[j - 1]:
                array[j], array[j - 1] = array[j - 1], array[j]
            else:
                break
        if printEach:
            print(array)


if __name__ == "__main__":
    array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
    print(f"Initial Array : {array}")
    insertion_sort(array)
    print(f"Final Sorted Array : {array}")
