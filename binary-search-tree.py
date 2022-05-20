#Binary search tree (BST) practice from Udacity course "Data Structures and Algorithms in Python"

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        start = self.root
        while start:
            if new_val < start.value:
                if start.left != None:
                    start = start.left
                else:
                    newNode = Node(new_val)
                    start.left = newNode
                    break
            elif new_val > start.value:
                if start.right != None:
                    start = start.right
                else:
                    newNode = Node(new_val)
                    start.right = newNode
                    break

    def search(self, find_val):
        start = self.root
        while start:
            if find_val == start.value:
                return True
            elif find_val < start.value:
                start = start.left
            elif find_val > start.value:
                start = start.right
        return False
    
# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print tree.search(4)
# Should be False
print tree.search(6)