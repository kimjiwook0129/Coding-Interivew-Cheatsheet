from collections import deque

class BinaryTree:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

    def preOrderPrint(self):
        print(self.data, end = " ")
        if self.left:
            self.left.preOrderPrint()
        if self.right:
            self.right.preOrderPrint()

    def inOrderPrint(self):
        if self.left:
            self.left.inOrderPrint()
        print(self.data, end = " ")
        if self.right:
            self.right.inOrderPrint()

    def postOrderPrint(self):
        if self.left:
            self.left.postOrderPrint()
        if self.right:
            self.right.postOrderPrint()
        print(self.data, end = " ")


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
    tree.levelOrderPrint() # 1, 2, 3, 4, 5, 6, 7, 8, 9
    print()