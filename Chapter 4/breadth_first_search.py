
#Define BST
#diagram to code
#top node data --> data in the node, Left child and right child (root)

##Preorder:print left tree breanch then treve back to print right
import collections


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

#create an adjency list
#use the existing traversal code
def makeList(r):
    if r is None:
        return
    else:
        #make an entry into the dictionary at each
        d[r.data] = []
        makeList(r.left)
        if r.left:
            d[r.data].append(r.left.data)
        if r.right:
            d[r.data].append(r.right.data)
        makeList(r.right)
    return d #modified dictionary

def bfs(al):
    #need a quesu and a list
    queue = collections.deque('g')
    visited = []
    #iterate the queue
    while queue:
        #node added to visited list and children
        node = queue.popleft()
        visited.append(node)
        for x in al[node]:
            queue.append(x)
    print(visited)

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

d = {}
aList = makeList(root)
for i in aList:
    print(f'{i}:{d[i]}')

bfs(aList)
#print all nodes inOrder --> nodes are visited in ascending order
