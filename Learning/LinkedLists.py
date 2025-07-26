# Linked List Implementation
class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
    def getData(self):
        return self.data
    def getNext(self):
        return  self.next

class LinkedList:
    def __init__(self):
        self.head = None
    #add element
    def insert(self, data, pos):
        newNode = Node(data)
        currentHead = self.head
        for i in range(pos):
            currentHead = currentHead.next
        newNode.next = currentHead
        currentHead.next = newNode




