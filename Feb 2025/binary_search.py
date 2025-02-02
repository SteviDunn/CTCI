#given an array of integers nums which is sorted in
#ascending order, and an integer target, write a function to search target
#in nums.
#if target exists, then return its index
#other wise return -1

#algo must be O(log n) complexity
#a problem has log n complexity if with each iteration it 
#halves the size of the problem its working on
#esentially dividing the data input into smaller parts until it reaches a solution
from typing import List

class Solution(object):
    def search(self, nums:List[int], target: int) -> int:
        #start in the middle and halve each time
        #we can do this because the list is sorted
        #nums = [-1, 3, 4, 6, 8, 9, 12, 15, 18]
        #target = 9

        #recursively find middle index?
        #middle = (start+end) /2
        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = (start+end) // 2
            num = nums[mid]
            if target == num:
                return mid
            if target > num:
                start = mid
            if target < mid:
                end = mid
        return -1

