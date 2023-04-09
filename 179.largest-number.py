from typing import List
#
# @lc app=leetcode id=179 lang=python3
#
# [179] Largest Number
#

# @lc code=start
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        new_list = list(map(str,nums))
        new_list.sort(key = lambda x: x*10, reverse=True)
        final = ''.join(new_list)
        if final[0] == '0':
            return '0'
        else:
            return final

   
# @lc code=end

# Steps I took to solve this problem:
# 1. I used a map function to change the list of integers to list of strings.
# 2. I used a lambda function to sort the list of strings by the first digit of each string. 
# I chose the first digit because it is the most significant digit and 
# I chose 10 because it is the largest number that can be formed by repeating the same digit.
# 3. I used a join function to join the list of strings into one string.
# 4. I used an if statement to check if the first digit of the string is 0, if it is, return 0, else return the string. 
# This is because if the first digit is 0, it means that the list of integers only contains 0s, and the largest number is 0.
# 5. I returned the string.



