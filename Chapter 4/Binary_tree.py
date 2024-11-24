#defining a binary searhc tree 
#Binary tree: each node at most 2 children
#Left child must always be less than the parent
#right child is greater than parent

#Define BST
#diagram to code
#top node data --> data in the node, Left child and right child (root)
class Node: 
    #need tree constructor for the first node and initilization
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data 