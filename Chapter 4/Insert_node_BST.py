
#Define BST
#diagram to code
#top node data --> data in the node, Left child and right child (root)
class Node: 
    #need tree constructor for the first node and initilization
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data 

    #need to add a method to add nodes
    def insert(self, data):
        #check if existing data is none
        if self.data is None:
            self.data = data
        else:
            if data < self.data:
                #go to left sub tree
                #check if none
                if self.left is None:
                    self.left = self.data
                else:
                    #need to recursively insert
                    #the left node is seen as a new
                    #beginning node of a tree recursive
                    self.left.insert(data)
            elif data > self.data:
                #go to left sub tree
                #check if none
                if self.right is None:
                    self.right = self.data
                else:
                    #need to recursively insert
                    #the left node is seen as a new
                    #beginning node of a tree recursive
                    self.right.insert(data)

if __name__ == "__main__":
    #create tree with 1 node
    root = Node('g')
    root.insert('c')