
#Define BST
#diagram to code
#top node data --> data in the node, Left child and right child (root)

##Preorder:print left tree breanch then treve back to print right
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
                    self.left = Node(data)
                else:
                    #need to recursively insert
                    #the left node is seen as a new
                    #beginning node of a tree recursive
                    self.left.insert(data)
            elif data > self.data:
                #go to left sub tree
                #check if none
                if self.right is None:
                    self.right = Node(data)
                else:
                    #need to recursively insert
                    #the left node is seen as a new
                    #beginning node of a tree recursive
                    self.right.insert(data)

def inOrderPrint(r):
    if r is None:  # Base case: empty subtree
        return
    else:
        #in order for left, print then right
        inOrderPrint(r.left)
        print(r.data)
        inOrderPrint(r.right)

def PreOrderPrint(r):
    if r is None:
        return
    else:
        #first print root
        print(r.data, end = " ")
        #then left branch
        PreOrderPrint(r.left)
        PreOrderPrint(r.right)

#PostOrder: root right left
def PostOrderPrint(r):
    if r is None:
        return
    print(r.data, end = " ")
    PostOrderPrint(r.right)
    PostOrderPrint(r.left)
    


if __name__ == "__main__":
    #create tree with 1 node
    root = Node('g')
    root.insert('c')
    root.insert('i')
    root.insert('b')
    root.insert('e')
    root.insert('h')
    root.insert('j')   

inOrderPrint(root)
PostOrderPrint(root)

#print all nodes inOrder --> nodes are visited in ascending order
