#Queue via Stacks: Implement a MyQueue
# class which implements a queue using two stacks. 
class Myqueue:
    #initialize the stacks
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x:int) -> None:
        self.s1.append(x)

    def pop(self):
        #when we pop for queue it's a First in First out structure
        #therefore when we make the first s1, to pop we need to take the 
        #first element we added which requires that we revese the stack in s2

        #reverse s1
        #first check if s2 is nonempty
        if not self.s2: #"if s2 is empty"
            #copy over all of s2 reversed
            while self.s1: #iterste over all of s1
                self.s2.append(self.s1.pop())
        #now we can pop off the front of the queue
        return self.s2.pop()
    
    #define the peek fucntion which returns the front of the queue
    def peek(self):
        #which are we peekig from?
        #we are peeking from the front of s2 becaue it is the front
        #first check that s2 is not empty
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        #return the top of s2
        return self.s2.pop()
