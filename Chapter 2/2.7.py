#Intersection: Given two (singly) linked lists, determine if the two lists intersect. 
#Return the intersecting node. Note that the intersection is defined based on reference, not value.
# That is, if the kth node of the first linked list is the exact same node (by reference) as the jth node of the second 
#linked list, then they are intersecting. 
#Hints:#20, #45, #55, #65, #76, #93, #111, #120, #129 
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

#functino to get the intersection point of two linked lists
def get_intersection(head1, head2):
    visited_nodes = {} #hash tabe made using set

    #traverse the first list and store all nodes in a set
    curr1 = head1
    while curr1 is not None:
        visited_nodes[curr1] =True 
        curr1 = curr1.next

    #traverse the second list and check if any node is in the set
    curr2 = head2
    while curr2 is not None:
        if curr2 in visited_nodes:
            return curr2 #intersection point found
        curr2 = curr2.next

    return None

if __name__ == "__main__":
    # Create two linked lists
    # 1st list: 10 -> 15 -> 30
    # 2nd list: 3 -> 6 -> 9 -> 15 -> 30
    # 15 is the intersection point

    # Creating the first linked list
    head1 = Node(10)
    head1.next = Node(15)
    head1.next.next = Node(30)

    # Creating the second linked list
    head2 = Node(3)
    head2.next = Node(6)
    head2.next.next = Node(9)
    head2.next.next.next = head1.next #defined intersection here

    # Finding the intersection point
    intersection_point = get_intersection(head1, head2)

    if intersection_point is None:
        print("No Intersection Point")
    else:
        print("Intersection Point:", intersection_point.data)

