from binarytree import printPostorder,printPreorder,printInorder,printLevelOrder

class Node:
    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

def search(root,key):
    if root is None or root.val == key:
        return root
    if root.data < key:
        return search(root.left,key)
    return search(root.right,key)

def insert(root,key):
    if root is None:
        return Node(key)
    else:
        if root.data == key:
            return root
        elif root.data < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

def minValueNode(node):
    current = node
    # loop down to find the leftmost leaf
    while (current.left is not None):
        current = current.left

    return current

def deleteNode(root, key):
    # Base Case
    if root is None:
        return root

    if key < root.key:
        root.left = deleteNode(root.left, key)

    elif (key > root.key):
        root.right = deleteNode(root.right, key)

    else:
       # Node with only one child or no child
        if root.left is None:
            temp = root.right
            root = None
            return temp

        elif root.right is None:
            temp = root.left
            root = None
            return temp

        # Node with two children:
        # Get the inorder successor
        # (smallest in the right subtree)
        temp = minValueNode(root.right)

        # Copy the inorder successor's
        # content to this node
        root.key = temp.key

        # Delete the inorder successor
        root.right = deleteNode(root.right, temp.key)

    return root

class BinarySearchTree:

    def __init__(self):
        self.root = None

    def search(self,key):
        return search(self.root,key=key)

    def insert(self,data):
        if self.root is None:
            self.root = Node(data)
        insert(self.root,data)

    def deleteNode(self,data):
        deleteNode(self.root,key=data)

    def minValue(self):
        temp = self.root
        while temp.left is not None:
            temp = temp.left
        return temp.data

"""
bst = BinarySearchTree()
bst.insert(8)
bst.insert(12)
bst.insert(63)
bst.insert(0)
bst.insert(100)
bst.insert(67)
"""





