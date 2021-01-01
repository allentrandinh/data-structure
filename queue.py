class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

class Queue():
    def __init__(self):
        self.front = None
        self.rear = None

    def isEmpty(self):
        return(self.front is None)

    def enQueue(self,data):
        new_node = Node(data=data)
        if self.front is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def deQueue(self):
        if self.front is None:
            print("Queue is empty")
            return
        self.front = self.front.next

    def display(self):
        if self.front is None:
            print("Queue is empty")
            return
        temp = self.front
        while temp:
            print(temp.data)
            temp = temp.next

class DequeNode:
    def __init__(self,data,next=None,prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DeQue:
    def __init__(self):
        self.root = None
        self.rear = None

    def isEmpty(self):
        return(self.root is None)

    def insertFront(self,data):
        new_node = DequeNode(data=data)
        if self.root is None:
            self.root = self.rear = new_node
        else:
            new_node.next = self.root
            self.root.prev = new_node
            self.root = new_node

    def insertLast(self,data):
        new_node = DequeNode(data=data)
        if self.rear is None:
            self.root = self.rear = new_node
        else:
            new_node.prev = self.rear
            self.rear.next = new_node
            self.rear = new_node

    def deleteFront(self):
        if self.root is None:
            print("DeQue is empty")
            return
        self.root = self.root.next
        del self.root.prev
        self.root.prev = None

    def deleteLast(self):
        if self.rear is None:
            print("DeQue is empty")
            return
        self.rear = self.rear.prev
        del self.rear.next.data
        self.rear.next = None

    def getRear(self):
        return(self.rear.data)

    def getFront(self):
        return(self.root.data)

    def display(self):
        if self.root is None:
            print("DeQue is empty")
            return
        temp = self.root
        while temp:
            print(temp.data)
            temp = temp.next
'''
deq = DeQue()
deq.display
deq.insertFront(98)
deq.insertLast(23)
deq.insertLast(4)
deq.insertFront(100)
print("********")
deq.display()
print("********")
deq.deleteFront()
deq.display()
'''




