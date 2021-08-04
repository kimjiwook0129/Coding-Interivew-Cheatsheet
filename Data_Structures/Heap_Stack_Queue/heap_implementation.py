import time


class MinHeap:
    def __init__(self, array):
        self.heap = self.buildHeap(array)

    # Complexities : Time O(N log N) | Space O(1)
    def buildHeap(self, array):
        lowestParentIdx = (len(array) - 2) // 2
        for idx in reversed(range(lowestParentIdx)):
            self.siftDown(idx, array)
        return array

    # Complexities : Time O(log N) | Space O(1)
    def insert(self, element):
        self.heap.append(element)
        self.siftUp(len(self.heap) - 1, self.heap)

    # Complexities : Time O(1) | Space O(1)
    def peek(self):
        return self.heap[0]

    # Complexities : Time O(log N) | Space O(1)
    def siftDown(self, curIdx, heap):
        endIdx = len(heap) - 1
        childOne = 2 * curIdx + 1
        while childOne <= endIdx:
            childTwo = childOne + 1 if childOne + 1 <= endIdx else -1
            idxSwap = childOne
            if childTwo != -1 and heap[childOne] > heap[childTwo]:
                idxSwap = childTwo
            if heap[idxSwap] < heap[curIdx]:
                self.swap(curIdx, idxSwap, heap)
                curIdx = idxSwap
                childOne = curIdx * 2 + 1
            else:
                return

    # Complexities : Time O(log N) | Space O(1)
    def siftUp(self, curIdx, heap):
        parent = (curIdx - 1) // 2
        while curIdx >= 0 and heap[curIdx] < heap[parent]:
            self.swap(parent, curIdx, heap)
            curIdx = parent
            parent = (curIdx - 1) // 2

    # Complexities : Time O(log N) | Space O(1)

    def remove(self):
        self.swap(0, len(self.heap) - 1, self.heap)
        top = self.heap.pop()
        self.siftDown(0, self.heap)
        return top

    def swap(self, idx1, idx2, heap):
        heap[idx1], heap[idx2] = heap[idx2], heap[idx1]


def print_commands():
    print('Commands : ')
    print('\'exit\' -> exit program | \'reset\' -> initialize the heap array')
    print('\'remove\' -> removes & prints the top, \'peek\' -> prints the top')
    print('\'print\' -> prints the current heap')
    print('\'insert\' -> inserts the given elements')


def invalid_action():
    print('Invalid command! try again...')
    time.sleep(1)
    print_commands()


if __name__ == "__main__":
    print_commands()

    user_heap = MinHeap([])
    while True:
        command = input('Type command : ')
        if command == 'exit':
            break
        if command == 'reset':
            user_heap = MinHeap([])
        elif command == 'remove':
            print(user_heap.remove())
        elif command == 'peek':
            print(user_heap.peek())
        elif command == 'insert':
            nums = list(map(int, input('Give me Numbers : ').split()))
            for i in range(len(nums)):
                user_heap.insert(nums[i])
        elif command == 'print':
            print(user_heap.heap)
        else:
            invalid_action()
        print(f'Current Heap : {user_heap.heap}')
    print("Program Exited")
