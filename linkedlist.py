import math

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head= None

    def display(self):
        if self.head is None:
            print("Empty List")
        else:
            temp = self.head
            while (temp):
                print(temp.data)
                temp = temp.next

    def push(self,data_to_be_added):
        new_node = Node(data_to_be_added)
        new_node.next = self.head
        self.head = new_node

    def addFrontNode(self,node_to_be_added):
        node_to_be_added.next = self.head
        self.head = node_to_be_added

    def insertAfter(self,data_to_be_added,previous_node_data):
        temp = self.head
        new_node = Node(data_to_be_added)
        while temp.data != previous_node_data:
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node

    def append(self,data_to_be_added):
        new_node = Node(data_to_be_added)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = new_node

    def deleteNode(self,data_to_be_deleted):
        #if node at the beginning, set beginning to second node
        '''
        :param data_to_be_deleted:
        :return: delete first occurence
        '''
        if self.head.data == data_to_be_deleted:
            self.head = self.head.next
        else:
            temp = self.head
            while temp.next.data != data_to_be_deleted:
                temp = temp.next
            if temp.next.next is None:
                #if node at the end, set end to prev node
                temp.next = None
            else:
                #otherwise, connect prev node w/ after node, free up space
                connecting_node = temp.next.next
                temp.next = None
                temp.next = connecting_node

    def deleteNodeAtPosition(self,position):
        '''
        :param position: 1-based position
        '''
        pos = 1
        #temp is the previous node
        temp = self.head
        while pos < position-1:
            temp = temp.next
            pos += 1
        connecting_node = temp.next.next
        temp.next = None
        temp.next = connecting_node

    def deleteList(self):
        temp = self.head
        while temp:
            next_node = temp.next
            del temp.data
            temp = next_node

    def length(self):
        length = 0
        temp = self.head
        while temp:
            length += 1
            temp = temp.next
        return(length)

    def search(self,data_to_be_searched):
        temp = self.head
        while temp.data != data_to_be_searched:
            if temp.next != None:
                temp = temp.next
            else:
                return(False)
        return(True)

    def getNode(self,position):
        '''
        :param position: 0-based
        '''
        pos = 0
        temp = self.head
        while pos < position:
            temp = temp.next
            pos += 1
        return(temp.data)

    def getNodefromEnd(self,position_from_end):
        '''
        :param position_from_end: 1-based from the end
        :return:
        '''
        total_length = self.length()
        position = total_length - position_from_end
        pos = 0
        temp = self.head
        while pos < position:
            temp = temp.next
            pos += 1
        return(temp.data)

    def getMiddleNode(self):
        '''
        :return: if number of elements is even, return the second among the 2 middle nodes.
        '''
        total_length = self.length()
        position = math.floor(total_length/2) + 1
        pos = 1
        temp = self.head
        while pos < position:
            temp = temp.next
            pos += 1
        return(temp.data)

    def countOccurrence(self,data_to_be_counted):
        count = 0
        temp = self.head
        while temp:
            if temp.data == data_to_be_counted:
                count += 1
            temp = temp.next
        return(count)

    def detectLoop(self):
        s = set()
        temp = self.head
        while temp:
            if temp in s:
                return(True)
            s.add(temp)
            temp = temp.next
        return(False)

    def removeDuplicates(self):
        '''
        keep first occurence of any value
        '''
        s = set()
        temp = self.head
        while temp:
            if temp.next.data in s:
                next_node = temp.next
                while next_node and (next_node.data in s):
                    next_node = next_node.next
                if next_node is None:
                    temp.next = None
                else:
                    temp.next = next_node
            s.add(temp.data)
            temp = temp.next

    def swapNode(self,first_data,second_data):
        #do nothing if two data is the same
        if first_data == second_data:
            return

        #find node of first data and node of second data
        prev_first = None
        first = self.head
        while (first.next != None) and (first.data != first_data):
            prev_first = first
            first = first.next

        prev_second = None
        second = self.head
        while (second.next != None) and (second.data != second_data):
            prev_second = second
            second = second.next

        if (second.next == None) and (second.data != second_data):
            print("Second data not in list")
            return

        if (first.next == None) and (first.data != first_data):
            print("First data not in list")
            return

        if prev_first != None:
            prev_first.next = second
        else:
            self.head = second

        if prev_second != None:
            prev_second.next = first
        else:
            self.head = first

        temp = first.next
        first.next = second.next
        second.next = temp

    def moveLasttoFirst(self):
        prev = None
        temp = self.head
        while temp.next != None:
            prev = temp
            temp = temp.next
        prev.next = None
        temp.next = self.head
        self.head = temp

    def intersectWithList(self,second_linked_list):
        #create new llist
        new_llist = LinkedList()

        #create set storing value of current linked list
        s = set()
        temp = self.head
        while temp != None:
            s.add(temp.data)
            temp = temp.next
        #loop thru each element in list 2
        temp_2 = second_linked_list.head
        while temp_2 != None:
            if temp_2.data in s:
                new_llist.append(temp_2.data)
            temp_2 = temp_2.next
#        new_llist.removeDuplicates()
        return(new_llist)

    def reverse(self):
        prev = None
        temp = self.head
        next = temp.next

        while next is not None:
            temp.next = prev
            #move all pointers by 1
            prev = temp
            temp = next
            next = temp.next

        #for last Node
        temp.next = prev
        self.head = temp

    def sort(self):
        if self.head is None:
            return
        current = self.head
        while current != None:
            next = current.next
            while next != None:
                if next.data < current.data:
                    temp = current.data
                    current.data = next.data
                    next.data = temp
                next = next.next
            current = current.next



