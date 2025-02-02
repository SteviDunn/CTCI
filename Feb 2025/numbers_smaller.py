#how many numbers are smaller than the current number
#given the array nums, for each num[i], find out how many
#numbers are smaller than it

#that is, for each num[i] you have to ocunt the number of valid js
#such that j != i and nums[j] < nums[i]
from typing import List

class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #loop through each number in the array 
        count_arr = [0] * len(nums)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] > nums[j]:
                    count_arr[i] += 1
        return count_arr