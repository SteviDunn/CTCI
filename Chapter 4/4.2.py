#minimal tree: given a sorted (increasing order) array 
#with unique integer eements, write an algorithm
#to create a binary search tree with minimal height
#remember: elemets on left side of the tree are less than 
#the root, right is greater than
#array is already sorted from lowest to heighest

#root is going to be the middle element recursively?

#Define class node to represent a node in the bst
class Node:
    #contructor of the Node class. 
    #initialize the node with the given data and two pointers
    #left and right
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
#define a recursive function to build bst
#arr is the sorted array
#start is the start of the array
#end is the end of the array
def Arr_to_BST(arr, start, end):
    #first check to see if we can perform the func
    if start > end: #not possible in ascending order
        return None
        #means there are no more elements to add to tree
    
    #fid mid point to be root node
    mid = start + (end-start) //2

    #create a new node with the value arr[mid]
    #this is the root of the current sub tree
    root = Node(arr[mid])
    #now, recursively contruct the left subtree using
    #the left half of the array 
    root.left = Arr_to_BST(arr, start, mid-1)

    #recursively contruct right subtree using
    #right half of the array
    root.right = Arr_to_BST(arr, mid+1, end)

    #return root returns the constructed subtree
    return root

#Define a function to perform pre-order traversal of bst
#pre-order traveral visits nodes in the order"
#root, left subtree, right subtree
def PreOrder(root):
    if root is None:
        return
    print(root.data, end="")
    PreOrder(root.left)
    PreOrder(root.right)

if __name__ == "__main__":
    arr = [1,2,3,4]
    root = Arr_to_BST(arr, 0, len(arr)-1)
    PreOrder(root)

        