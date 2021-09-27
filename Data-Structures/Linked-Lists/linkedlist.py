from node import Node

class LinkedList:
    def __init__(self):
        self.head = None
    
    def length(self):
        cur = self.head
        count = 0
        while cur:
            count += 1
            cur = cur.getNext()
        return count

    def insert(self, data, pos = 0):
        if pos > self.length(): print("Pos bigger than the length, cannot be done")
        else:
            newNode = Node(data)
            if pos == 0:
                newNode.setNext(self.head)
                self.head = newNode
            else:
                pos -= 1
                cur = self.head
                while pos > 0:
                    cur = cur.getNext()
                    pos -= 1
                newNode.next = cur.getNext()
                cur.next = newNode

    def delete(self, pos):
        if pos >= self.length(): print("Pos bigger than the length, cannot be done")
        else:
            if pos == 0:
                self.head = self.head.getNext()
            else:
                prev = self.head
                cur = self.head.getNext()
                pos -= 1
                while pos > 0:
                    prev, cur = prev.getNext(), cur.getNext()
                    pos -= 1
                prev.setNext(cur.getNext())

    def print(self):
        cur = self.head
        while cur:
            print(cur.getValue(), end = " ")
            cur = cur.getNext()
        print()

if __name__ == "__main__":
    lst = LinkedList()
    lst.insert(4); lst.insert(3); lst.insert(2); lst.insert(1)
    lst.insert(2.5, 2)
    lst.print()
    lst.delete(5); lst.delete(1)
    lst.print()