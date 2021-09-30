from collections import deque

# Same BinaryTree, but the print methods are implemented using iterations
class BinaryTree:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

    def preOrderPrint(self):
        s = deque([self])
        while s:
            curNode = s.pop()
            print(curNode.data, end = " ")
            if curNode.right:
                s.append(curNode.right)
            if curNode.left:
                s.append(curNode.left)

    def inOrderPrint(self):
        s = deque([])
        while True:
            if self:
                s.append(self)
                self = self.left
            else:
                if len(s) == 0: break
                self = s.pop()
                print(self.data, end = " ")
                self = self.right

    def postOrderPrint(self):
        s1 = deque([self])
        s2 = deque([])
        while s1:
            curNode = s1.pop()
            s2.append(curNode)
            if curNode.left:
                s1.append(curNode.left)
            if curNode.right:
                s1.append(curNode.right)
        while s2:
            print(s2.pop().data, end = " ")

    def postOrderPrintOneStack(self):
        pass

    def levelOrderPrint(self):
        q = deque([])
        q.append(self)
        while q:
            curNode = q.popleft()
            print(curNode.data, end = " ")
            if curNode.left:
                q.append(curNode.left)
            if curNode.right:
                q.append(curNode.right)

if __name__ == "__main__":
    tree = BinaryTree(1, BinaryTree(2, BinaryTree(4)), \
        BinaryTree(3, BinaryTree(5, None, BinaryTree(7)), BinaryTree(6, BinaryTree(8), BinaryTree(9))))
    tree.preOrderPrint() # 1, 2, 4, 3, 5, 7, 6, 8, 9
    print()
    tree.inOrderPrint() # 4, 2, 1, 5, 7, 3, 8, 6, 9
    print()
    tree.postOrderPrint() # 4, 2, 7, 5, 8, 9, 6, 3, 1
    print()
    # tree.postOrderPrintOneStack() # 4, 2, 7, 5, 8, 9, 6, 3, 1
    # print()
    tree.levelOrderPrint() # 1, 2, 3, 4, 5, 6, 7, 8, 9
    print()