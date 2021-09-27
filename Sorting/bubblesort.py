# Bubble Sort [버블 정렬]
# Complexities : Time O(N^2)
# Best Time Complexity : O(N)

def bubblesort(array):
    sorted = False
    for i in range(len(array) - 1, -1, -1):
        sorted = True
        for j in range(i):
            if array[j] > array[j + 1]:
                sorted = False
                array[j], array[j + 1] = array[j + 1], array[j]
        if sorted: break
    
if __name__ == "__main__":
    array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
    print(f"Initial Array : {array}")
    bubblesort(array)
    print(f"Final Sorted Array : {array}")
