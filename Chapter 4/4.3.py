#List of Depths: Given a binary tree, design an algorithm which 
#creates a linked list of all the nodes at each depth 
# (e.g., if you have a tree with depth D, you1I have D linked lists). 

#first create the TreeNode and Listnode to add to 

class TreeNode:
    def __init__(self, val=0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class LinkedListNode:
    def __init__(self, val=0, next = None):
        self.val = val
        self.next = next

#define the main algo to bfs the tree and add the levels tolinked lists
def tree_to_linked_list(root):
    #first test edge case of empty tree
    if not root:
        return []
    #initialize the list of our final result
    result = []
    #also initialize the queue we will use
    queue = [root]

    #use a while loop to trverse the whole tree, we make it dependent on
    #the queue because for each level we will add and remove the values
    while queue: 
        #for the for loop we need the current depth length
        level_length = len(queue)
        #also need to initialize the pointers for the linked lists levels
        level_list = None
        tail = None

        #process each node into ll for the current depth
        for i in range(level_length):
            #dequeue the first node and add the next nodes from the other levels
            tree_node = queue.pop(0)

            #create a new linked list for the level and the valeus popped from the queue
            linked_list_node = LinkedListNode(tree_node.val)

            #if level list is none this is the first node so we need to initialize the pointers with these values
            if level_list is None:
                level_list = linked_list_node
                tail = linked_list_node
            #Enque the left and right children to the queue so that they can be added to thier own lls
            if tree_node.left:
                queue.append(tree_node.left)
            if tree_node.right:
                queue.append(tree_node.right)
            
            #add the current depth list to the total list
            result.append(level_list)
    return result

# Example Usage:
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

print(tree_to_linked_list(root))