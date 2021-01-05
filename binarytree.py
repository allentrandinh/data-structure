class Node:
    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right
    def getVal(self):
        return self.data
    def setVal(self,data):
        self.data = data
    def setRight(self,right_node):
        self.right = right_node
    def setLeft(self, left_node):
        self.left = left_node
    def getRight(self):
        return self.right
    def getLeft(self):
        return self.left

def printInorder(root):
    if root:
        printInorder(root.left)
        print(root.data)
        printInorder(root.right)

def printPostorder(root):
    if root:
        printPostorder(root.left)
        printPostorder(root.right)
        print(root.data)

def printPreorder(root):
    if root:
        print(root.data)
        printPreorder(root.left)
        printPreorder(root.right)

def printLevelOrder(root):
    if root is None:
        return

    queue = []
    queue.append(root)

    while (len(queue) >0):
        print(queue[0].data)
        node = queue.pop(0)
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)

def height(node):
    if node is None:
        return 0
    return (1 + max(height(node.left), height(node.right)))

def diameter(root):
    if root is None:
        return 0
    lheight = height(node=root.left)
    rheight = height(node=root.right)
    ldiameter = diameter(root.left)
    rdiameter = diameter(root.right)
    return max(lheight + rheight + 1, max(ldiameter, rdiameter))


def maxDepth(node):
    if node is None:
        return 0;
    else:
        # depth of each subtree
        lDepth = maxDepth(node.left)
        rDepth = maxDepth(node.right)
        return(max(lDepth,rDepth)+1)


def printAncestors(root,target):
    # Base case
    if root == None:
        return False
    if root.data == target:
        return True
    # If target is present in either left or right subtree
    # of this node, then print this node
    if (printAncestors(root.left, target) or
            printAncestors(root.right, target)):
        print(root.data),
        return True
    return False

def areIdentical(root1, root2):
    # Base Case
    if root1 is None and root2 is None:
        return True
    if root1 is None or root2 is None:
        return False
    return (root1.data == root2.data and
            areIdentical(root1.left, root2.left) and
            areIdentical(root1.right, root2.right))

def isSubtree(tree,potential_substree):
    if potential_substree is None:
        return True
    if tree is None:
        return False
    if (areIdentical(tree, potential_substree)):
        return True
    return isSubtree(tree.left, potential_substree) or isSubtree(tree.right, potential_substree)


class BinaryTree():

    def __init__(self):
        self.root = None

    def diameter(self):
        return(diameter(self.root))

    def maxDepth(self):
        return(maxDepth(self.root))

    def insert(self,data):
        new_node = Node(data=data)
        if self.root is None:
            self.root = new_node
            return
        q = []
        q.append(self.root)
        while len(q):
            temp = q[0]
            q.pop(0)
            if temp.left is None:
                temp.left = new_node
                break
            else:
                q.append(temp.left)

            if (not temp.right):
                temp.right = newNode(key)
                break
            else:
                q.append(temp.right)


"""
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

tree = BinaryTree()
tree.root = root

print(tree.diameter())
"""


