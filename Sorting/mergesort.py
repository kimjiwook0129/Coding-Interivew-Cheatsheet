# Merge Sort [합병 정렬]
# Complexities : Time O(N log N) | Space O(N)

def merge(array, left, mid, right):
    leftLen, rightLen = mid - left + 1, right - mid
    leftArr, rightArr = [0] * leftLen, [0] * rightLen
    l, r, merge_idx = 0, 0, left

    for i in range(leftLen):
        leftArr[i] = array[left + i]
    for i in range(rightLen):
        rightArr[i] = array[mid + 1 + i]

    while l < leftLen and r < rightLen:
        if leftArr[l] <= rightArr[r]:
            array[merge_idx] = leftArr[l]
            l += 1
        else:
            array[merge_idx] = rightArr[r]
            r += 1
        merge_idx += 1

    while l < leftLen:
        array[merge_idx] = leftArr[l]
        l += 1
        merge_idx += 1
    while r < rightLen:
        array[merge_idx] = rightArr[r]
        r += 1
        merge_idx += 1


def mergesort(array, left, right):
    if left < right:
        mid = (left + right) // 2
        mergesort(array, left, mid)
        mergesort(array, mid + 1, right)
        merge(array, left, mid, right)


if __name__ == "__main__":
    array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
    print(f"Initial Array : {array}")
    mergesort(array, 0, len(array) - 1)
    print(f"Final Sorted Array : {array}")
