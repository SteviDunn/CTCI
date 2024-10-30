#Stack Min: How would you design a stack which,
#  in addition to push and pop, has a function min 
#which returns the minimum element? Push, 
# pop and min should all operate in 0(1) time. 
#Hints: #27, #59, #78
class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minStack:
            val = min(val, self.minstack[-1])
        else:
            val = val
        self.minStack.append(val)
    
    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]

    