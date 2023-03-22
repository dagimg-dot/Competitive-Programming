from typing import List
#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hash = {}
        for i in range(len(nums)):
            if nums[i] not in hash.keys():
                hash[nums[i]] = 1
            else:
                hash[nums[i]] += 1

        for key,value in hash.items():
            if value == 1:
                return key
                
# @lc code=end



