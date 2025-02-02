#max number of coins you can get
#there are 3n piles of coins of varying size
#3n=  piles is 3, 6, 9, 12 ect.... in the array (a,b,c)...
#we dont know how many coins in each pile 
#you and your friends take piles of coins as follwos:
# 
# in each step you choose any 3 piles of coins (alwasy choose max three piles first)
# of your choice, alice will pick the pile with max num coins
# you will pick next pile with max num coins 
# bob gets the last pile 
# repeat until there are no coins left 
# 
# Given an array of integers piles where piles[i] is the
# num coins in ith pile
# 
# return the max num of coins you can have
#


class Solution(object):
    def maxCoins(self, piles):
        #logic: to maximize returns for yoursels, always choose
        #the first two highest and then the lowest for bob

        #first, the constraints
        if len(piles) < 3 or len(piles)>= 10**5:
            return False
            
        calculating = True
        Alice_arr = []
        Me_arr = []
        Bob_arr =[]
        while (calculating):
            for i, value in enumerate(piles):
                if len(piles[i]) <=1 or len(piles[i]>= 10**4):
                    return False
            #how to iterate and update the array?
                pile = piles
            #find first highest value, add it to alice, then .pop from piles?
                Alice = Alice_arr.append(max(pile))
                pile.pop(Alice)
            #then find highest value of this iteration add it to me
                Me = Me_arr.append(max(pile))
                pile.pop(Me)

                Bob = Bob_arr.append(min(pile))
            #find lowest value in the array and add to bob
            #update the array for new loop?


#New Approach: 
#sort the array in descending order
#always take the second largest pile from every group of three 
#alce takes the most, bob takes the least
#Remember to take advantage of the structure!!!

#we want best case scenario for us which is the two max numbers
#and then the lowest
class Solution(object):
    def maxCoins(self, piles):
        #sort the list
        sorted_piles = sorted(piles, reverse = True)
        #iterate two from the right and 1 from the left
        #iterate over the number of piles n/3 not each element
        our_value = 0 
        for i in range(len(piles)//3):
            #triplet, highest, secind heighest, lowest
            triplet = (sorted_piles[i*2], sorted_piles[(i*2)+1], sorted_piles[len(sorted_piles)-1 - (i*2)])
        #add up 2nd biggest item in each triplet 
            our_value +=  sorted_piles[(i*2)+1]