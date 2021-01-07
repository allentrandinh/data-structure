from binarytree import printPostorder,printPreorder,printInorder,printLevelOrder

class BinarySearchTree:
    def __Node:
        def __init__(self,val,left=None,right=None):
            self.val = val
            self.left = left
            self.right = right
        def getVal(self):
            return self.val
        def setVal(self,val):
            self.val = val
        def setRight(self,right_node):
            self.right = right_node
        def setLeft(self, left_node):
            self.left = left_node
        def getRight(self):
            return self.right
        def getLeft(self):
            return self.left
        def __iter__(self):
            if self.left != None:
                for element in self.left:
                    yield element
            yield self.val

            if self.right != None:
                for element in self.right:
                    yield element

    def __init__(self):
        self.root = None

    def insert(self,val):
        @staticmethod
        def __insert(root,val):
            #if root is None, return root to insert in
            if root == None:
                return BinarySearchTree.__Node(val)
            #find appropriate location to insert, recursively return root at each level till self.root
            if val < root.getVal():
                root.setLeft(__insert(root.getLeft(),val))
            else:
                root.setRight(__insert(root.getRight(), val))
            return root
        self.root = __insert(self.root,val)

    def __iter__(self):
        if self.root != None:
            return self.root.__iter__()
        else:
            return [].__iter__()

    def search(self):
        def __search(root,key):
            if root is None or root.val == key:
                return root
            elif root < key:
                return(search(root.left,key))
            else:
                return(search(root.right,key))
        return(__search(self.root,key=key))

    def deleteNode(self,val):
        def __deleteNode(root,key):
            def minValueNode(node):
                current = node
                # loop down to find the leftmost leaf
                while (current.left is not None):
                    current = current.left

                return current
            #cant find key, return root
            if root is None:
                return root

            if key < root.val:
                root.left = __deleteNode(root.left, key)

            elif key > root.val:
                root.right = __deleteNode(root.right, key)

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
                root.right = __deleteNode(root.right, temp.key)

            return root
        self.root = __deleteNode(self.root,key=val)

class AVLTree:
    class AVLNode:
        def __init__(self,val,balance=0,left=None,right=None):
            self.val = val
            self.left = left
            self.right = right
            self.balance = balance
            self.height = 0

        def height(root):
            if root is None:
                return 0
            return (1 + max(height(node.left), height(node.right)))

        def __repr__(self):
            return f"AVLTree.AVLNode({repr(self.val)},balance {repr(self.balance)}, " \
                   f"left = {repr(self.left)}, right = {repr(self.right)})"

        def balance(root):
            return height(root.right) - height(root.left)

        def update(self):
            self.height = height(self)
            self.balance = balance(self)

    def __init__(self, root = None):
        self.root = root

    def rightRotate(pivot):
        left_node = pivot.left
        pivot.left = left_node.right
        left_node.right = pivot
        pivot.update()
        left_node.update()
        return left_node

    def leftRotate(pivot):
        right_node = pivot.right
        pivot.right = right_node.left
        right_node.left = pivot
        pivot.update()
        right_node.update()
        return right_node

    def rotation(pivot):
        if pivot.balance == -2:
            # new node inserted in direction of imbalance
            if pivot.left.balance <= 0:
                rotated_root = rightRotate(pivot)
            else:
                pivot.left = leftRotate(pivot.left)
                rotated_root = rightRotate(pivot)
        if pivot.balance == 2:
            if pivot.right.balance >= 0:
                rotated_root = leftRotate(pivot)
            elif pivot.right.balance == -1:
                pivot.right = rightRotate(pivot.right)
                rotated_root = leftRotate(pivot)
        return rotated_root

    def height(root):
        if root is None:
            return 0
        return (1 + max(height(node.left), height(node.right)))

    def update(node):
        node.height = height(node)
        node.bf = balance


    def insert(root,value):
        #base call
        if root is None:
            return AVLNode(value)
        if value < root.val:
            root.left = insert(root.left,value)
        else:
            root.right = insert(root.right,value)

        root.update()
        return rotation(root)

    def insertNode(self,value):
        self.root = insert(self.root,value)

    def delete(self,value):
        def __deleteNode(root,key):

            #retunr leftmost leaf
            def minValueNode(node):
                current = node
                while (current.left is not None):
                    current = current.left
                return current

            #cant find key, return root
            if root is None:
                return root

            if key < root.val:
                root.left = __deleteNode(root.left, key)

            elif key > root.val:
                root.right = __deleteNode(root.right, key)

            else:
                # Node with only one child or no child
                if root.left is None:
                    temp = root.right
                    root = None
                    temp.update()
                    return rotation(temp)

                elif root.right is None:
                    temp = root.left
                    root = None
                    temp.update()
                    return rotation(temp)

                # Node with two children:
                # Get the inorder successor
                # (smallest in the right subtree)
                temp = minValueNode(root.right)

                # Copy the inorder successor's
                # content to this node
                root.key = temp.key

                # Delete the inorder successor
                root.right = __deleteNode(root.right, temp.key)
                root.update()
            return rotation(root)
        self.root = __deleteNode(self.root,key=val)




"""
bst = BinarySearchTree()
bst.insert(8)
bst.insert(12)
bst.insert(63)
bst.insert(0)
bst.insert(100)
bst.insert(67)
"""





