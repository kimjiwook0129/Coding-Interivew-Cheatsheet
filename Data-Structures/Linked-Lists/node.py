class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

    def getValue(self):
        return self.value
    
    def setValue(self, value):
        self.value = value
    
    def getNext(self):
        return self.next

    def setNext(self, next):
        self.next = next
