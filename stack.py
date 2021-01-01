class StackNode:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.root = None

    def isEmpty(self):
        return True if self.root is None else False

    def push(self,data):
        new_node = StackNode(data=data)
        new_node.next = self.root
        self.root = new_node

    def pop(self):
        if (self.isEmpty()):
            print("Stack is empty")
            return
        temp = self.root
        self.root = self.root.next
        popped = temp.data
        return popped

    def peek(self):
        if (self.isEmpty()):
            print("Stack is empty")
            return
        return self.root.data

    def reverse(self):
        reversed_stack = Stack()
        if self.isEmpty():
            print("Stack is empty")
            return
        while self.isEmpty() is not True:
            reversed_stack.push(self.pop())
        self.root = reversed_stack.root
        del reversed_stack

    def display(self):
        temp = self.root
        while temp:
            print(temp.data)
            temp = temp.next

    def sort(self):
        values = []
        while self.isEmpty() is not True:
            values.append(self.root.data)
            self.pop()
        values.sort(reverse=False)
        for each_value in values:
            self.push(each_value)



def areBracketsbalance(expression):
    close_stack = []
    open_brac = ["(","[","{"]
    close_brac = [")","]","}"]
    for char in expression:
        if char in open_brac:
            close_stack.append(close_brac[open_brac.index(char)])
        elif char in close_brac:
            if len(close_stack)==0:
                return(False)
            elif char == close_stack[-1]:
                close_stack.pop()
            else:
                return(False)
    if len(close_stack) ==0:
        return(True)
    else:
        return(False)


