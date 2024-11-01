#Stack of plates
#implement a data structure that mimics some threshold
#create a new stack once the previous one exceeds 
#capacity
class SetofStacks:
    #initialize the function
    def __init__(self, capacity: int) -> None:
        #define and empty stack
        self.stack = []
        #define the capacity
        self.capacity = capacity
    #first define the push function
    def push(self, val: int) -> None:
        #check to see if this is an empty array or not, do we need to initialize?
        if self.stack == []:
            #if the stack is empty we first have to initialize a sub stack into the stack
            self.stack.append([val])
        else:
            #now check to see if there is still room in the current stack (at capacity or not)
            if len(self.stack[-1]) >= self.capacity: #if the len of current stack is at or over capacity then we make a new stack
                self.stack.append([val])
            else: #else if theres room just append the val to the current stack
                self.stack[-1].append(val)


    #next define the pop function
    def pop(self):
        #define the popped item
        popped = self.stack[-1][-1]
        #check to see if the stack is empty or not
        if self.stack == []:
            raise NameError 
        else: #we have established the stakc is nonempty
            #check if the stack is the last elemet
            if len(self.stack[-1]) == 1:
                del self.stack[-1]
            else: 
                del self.stack[-1][-1]

        return popped