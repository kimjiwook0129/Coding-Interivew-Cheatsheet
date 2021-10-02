class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

    def __repr__(self):
        mystr = ""
        while self:
            mystr = str(self.data) + mystr
            self = self.next
        return mystr
    
    def linkedSum(self, first, second):
        carry = 0
        prev = None
        while first or second:
            firstVal = first.data if first else 0
            secondVal = second.data if second else 0
            sumVal = firstVal + secondVal + carry
            self.data = sumVal % 10
            carry = sumVal // 10
            if first: first = first.next
            if second: second = second.next
            self.next = Node(0)
            prev = self
            self = self.next
        prev.next = None

if __name__ == "__main__":
    a = Node(3, Node(1, Node(5))) # 513
    b = Node(4, Node(9, Node(1, Node(4)))) # 4194
    c = Node(0)
    c.linkedSum(a, b)
    print(repr(c)) # 4707
    a0 = Node(0)
    d = Node(0)
    d.linkedSum(a0, a0)
    print(repr(d)) # 0