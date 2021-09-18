import math
from collections import deque

def getDigitAt(num, d):
    num = str(num)
    return 0 if len(num) <= d else int(num[len(num) - 1 - d])

def radixsort(array):
    dq = [deque([]) for _ in range(10)]
    digits = int(math.log10(max(array))) + 1
    for d in range(digits):
        for i in range(len(array)):
            cur = getDigitAt(array[i], d)
            dq[cur].append(array[i])
        idx = 0
        for i in range(len(dq)):
            while dq[i]:
                array[idx] = dq[i].popleft()
                idx += 1 
    return array

if __name__ == "__main__":
    array = [17, 45, 39, 50, 34, 11, 6, 12, 334, 38]
    print(f"Initial Array : {array}")
    radixsort(array)
    print(f"Final Sorted Array : {array}")
