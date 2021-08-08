# Count Sort [계수 정렬]
# Complexities : Time O(N + K) | Space O(N + K)
#   Where K is the largest positive integer in the array
#   Count Sort can only be used when the array is finitely ranged with integers
#   Not too efficient in terms of Space Complexity if some data are too distant from each other

from timeit import default_timer

# Method 1


def countsort(array, printEach=True):
    countArray = [0] * (max(array) + 1)
    for elem in array:
        countArray[elem] += 1

    newArray = []
    for idx in range(1, len(countArray)):
        for _ in range(countArray[idx]):
            newArray.append(idx)
    return newArray

# Method 2
# Method 2 is about twice faster


def countsort2(array, printEach=True):
    countArray = [0] * (max(array) + 1)
    for elem in array:
        countArray[elem] += 1

    newArray = [0] * len(array)
    for i in range(1, len(countArray)):
        countArray[i] += countArray[i - 1]
    for i in range(len(array) - 1, -1, -1):
        elem = array[i]
        countArray[elem] -= 1
        newArray[countArray[elem]] = elem

    return newArray


if __name__ == "__main__":
    array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
    print(f"Initial Array : {array}")
    array = countsort2(array)
    print(f"Final Sorted Array : {array}")

    '''
    start = default_timer()
    array = countsort(array)
    end = default_timer()
    print(f"First Method : {end - start}s")
    start = default_timer()
    array = countsort2(array)
    end = default_timer()
    print(f"Second Method : {end - start}s")
    '''
