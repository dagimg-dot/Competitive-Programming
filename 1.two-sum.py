#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i!=j and nums[i] + nums[j] == target:
                    return [i,j]
# @lc code=end

# The steps I took to solve this problem:
# 1. I set up a nested for loop that runs through the elements of nums list.
# 2. It returns the first occurrence where the elements add up to a target.
# 3. It ignores the case where both the elements to add are equal.


        
