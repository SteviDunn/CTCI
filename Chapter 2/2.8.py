#Loop Detection: Given a circular linked list, 
# implement an algorithm that returns the node at the 
# beginning of the loop. 
# DEFINITION 
# Circular linked list A (corrupt) linked list 
# in which a node's next pointer points to an earlier node,
#  so as to make a loop in the linked list. 
# EXAMPLE 
# Input: 
# Output: 
# A-> B -> C -> D -> E -> C[thesameCasearlier] 
# C 
# Hints: #50, #69, #83, #90

#could i also use a hash table for this and loop through?
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

#detect loop code
def detect_loop(head):
     visited_nodes = {}

     curr = head
     while curr is not None:
        if curr in visited_nodes:
            return curr
        visited_nodes[curr] = True
        curr = curr.next
     return None 
    
if __name__ in "__main__":
    head = Node(10)
    head.next = Node(15)
    head.next.next = Node(4)

    head.next.next.next = head

    loopNode = detect_loop(head)
    if loopNode:
        print(loopNode.data)
    else:
        print(-1)
