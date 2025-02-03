#delete nodes and return a forest
#given teh root of a binary tree, each node has a distinct val
#after deleting all nodes within a value in to_delete, 
#we are left with a forest (a disjoint union of trees)
#return the roots of the trees in the remaining forest
#in any order

#understanding the problem:
#input: root, to_delete
#output: roots of the trees of remaining forest

class Treenode(object):
    def __init__(self, val=0, left = None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    #keep track of output as a global parameter of the class
    def __init__(self):
        self.output = []


    def delNodes(self, root, to_delete):
        #traverse the root with bfs or dfs and compare values to to_delete
        #work top down with bfs

        if root.val not in to_delete:
            self.output.append(root)
        #use a queue
        queue = [root]
        while queue:
            node = queue.pop(0)
            
            if node.val in to_delete:
                #call delete recursively
                if node.left:
                    self.delNodes(node.left, to_delete)
                if node.right:
                    self.delNodes(node.right, to_delete)
            else:
                #check to see if node left anf right exists
                if node.left:
                    #keep searching
                    queue.append(node.left)
                    #check if the node is deleted
                    if node.left.val in to_delete:
                        #update
                        node.left = None

                if node.right:
                    queue.append(node.right)
                    if node.right.val in to_delete:
                        node.right = None

        return self.output
        #delete nodes that are delete nodes (replace with null?)
        #save node to new list as deleted or not