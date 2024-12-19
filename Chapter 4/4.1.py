#Route Between Nodes: Given a directed graph, design an
# algorithm to find out whether there is a 
# route between two nodes.

#define the function for route between nodes
def is_route(graph, start_node, end_node):

    #first define how we are going to do this
    #use a stack to hold a temp vriabe to chek if it is the target node or if it has already been visited for the directed graph

    #define how we will store the visited nodes
    visited = set()

    #define the stack and starting location
    stack  = [start_node]


    #define edge case first
    if start_node == end_node:
        return True
    
    #define the main loop for iteration
    #while the stack has something in it
    while stack:
        current = stack.pop()
        #pop off from stack to hold in current to compare to other nodes
        if current in visited:
            continue
        #current is the current stack value
        #the current value is added to current
        visited.add(current)

        #new internal loop to go through the directed graph
        for neighbor in graph.get(current, []):
            #check if any of the values from current's [] contain the target node
            if neighbor == end_node:
                return True
            #if this is not the case then we need to change stack to the values within [] and go from there
            #BUt only if neighbor is not in viited already otherwise we woud just loop 
            if neighbor not in visited:
                stack.append(neighbor) 
    return False #return false if there is nothing else in stack to break out 


graph = {
    'A': ['B'],
    'B': ['C'],
    'C': [],
    'D': ['A', 'C']
}

start_node = 'A'
end_node = 'C'

print(is_route(graph, start_node, end_node))  # Output: True
