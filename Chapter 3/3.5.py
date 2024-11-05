#Sort Stack: Write a program to sort a stack such that the smallest 
# items are on the top. 
# You can use an additional temporary stack, 
# but you may not copy the elements into any other data structure 
#(such as an array). The stack supports the following operations:
#  push, pop, peek, and is Empty

def SortStack(x):
    curr = 0
    temp = []
    while x != []: #while the x input array is not empty we will take off the end and hold it in the current positon
        curr  = x.pop()
        #now we need to check if the temp array is empty or if the curr element is > the top element of the temp array
        #note, the temp array will be stored from lowest to heighest so we can reverse it at the end
        if len(temp) == 0 or curr > temp[-1]:
            temp.append(curr)
        else:
            j=True
            while j: #go into the next while loop to check subsequent elemns 
                if curr < temp[-1]:
                    #we need to put the top element of temp back to x until the curr element can be inserted into the temp
                    x.append(temp.pop())
                    if len(temp) == 0:
                        j =  False

                else:
                    j= False
            temp.append(curr)
        x.append(temp)
        return x