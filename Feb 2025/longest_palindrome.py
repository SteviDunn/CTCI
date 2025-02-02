#given a string s which consists of lowercase and uppercase letters
#return the length of the longest palindrome that can be built
#with the letters

#letters are case sensitive "Aa" is not a palindrome

class Solution(object):
    def longestPalindrome(self, s):
        
        #same forward and reverse
        #must be flippable
        #all digits must be even except the middle
        #save the number of values of each letter in a dictionary
        #the longest palendrome that can be built is the sum
        #of the even letters plus one odd

        #initialize dict
        count = {}

        # add all characters to the dict
        for char in s:
            count[char] = count.get(char, 0) +1

        #now check now many even counts and how many odd counts
        even = 0
        odd = 0
        for char in count:
            if count[char]%2 == 0: 
                even += count[char]
            if count[char]%2 != 0:
                odd += count[char]

        if odd >= 1:
            max_len_pal = even + 1
        else:
            max_len_pal = even
        
        return max_len_pal
                
            



