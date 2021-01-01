class Node:
    def __init__(self,data,prev=None,next=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList:

    def __init__(self):
        self.head = None

    def push(self,data):
        new_node = Node(data=data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def display(self):
        if self.head is None:
            print("List is empty")
        else:
            temp = self.head
            while temp is not None:
                print(temp.data)
                temp = temp.next

    def insertNodeAfter(self,data_to_be_added,data_of_prev_node):
        new_node = Node(data=data_to_be_added)
        temp = self.head
        while (temp.data != data_of_prev_node) and (temp != None):
            temp = temp.next
        if temp is None:
            print("previous data not in list")
            return
        after_node = temp.next
        if after_node is None:
            temp.next = new_node
            new_node.prev = temp
        else:
            temp.next = new_node
            new_node.prev = temp
            new_node.next = after_node
            after_node.prev = new_node

    def insertNodeBefore(self,data_to_be_added, data_of_after_node):
        new_node = Node(data=data_to_be_added)
        temp = self.head
        if temp.data == data_of_after_node:
            temp.prev = new_node
            new_node.next = temp
            self.head = new_node
            return
        while (temp.data != data_of_after_node) and (temp != None):
            temp = temp.next
        if temp is None:
            print("data of after node does not exist")
            return
        prev_node = temp.prev
        #rearrange connections
        temp.prev = new_node
        new_node.next = temp
        prev_node.next = new_node
        new_node.prev = prev_node

    def append(self,append_data):
        if self.head is None:
            self.head = Node(data=append_data)
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        new_node = Node(append_data)
        temp.next = new_node
        new_node.prev = temp

    def length(self):
        if self.head is None:
            print("List is empty")
            return
        temp = self.head
        count = 0
        while temp is not None:
            count += 1
            temp = temp.next
        return(count)

    def deleteNode(self,data_tobedeleted):
        '''
        delete first occurence of specified data
        '''
        if self.head is None:
            print("List is empty")
            return
        temp = self.head
        if temp.data == data_tobedeleted:
            self.head = temp.next
            del temp
            return
        while (temp.data != data_tobedeleted) and (temp is not None):
            temp = temp.next
        if temp is None:
            print("Specified data is not in List")
            return
        prev_node = temp.prev
        after_node = temp.next
        if after_node is None:
            prev_node.next = None
            return
        prev_node.next = after_node
        after_node.prev = prev_node
        del temp

    def reverse(self):
        if self.head is None:
            print("List is empty")
            return
        prev = None
        current = self.head
        after = current.next

        while current.next is not None:
            current.next = prev
            current.prev = after
            prev = current
            current = current.prev
            after = current.next
        current.next = prev
        self.head = current






