from typing import List
#
# @lc app=leetcode id=1365 lang=python3
#
# [1365] How Many Numbers Are Smaller Than the Current Number
#

# @lc code=start
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        num = [0]*len(nums)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if j == i:
                    continue
                if nums[j] < nums[i]:
                    num[i] += 1

        return num
        
# @lc code=end



