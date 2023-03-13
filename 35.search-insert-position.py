from typing import List

#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        output = 0
        if target in nums:
            output = [i for i in range(len(nums)) if target == nums[i]]
        else:
            nums.append(target)
            nums.sort()
        
        for i in range(len(nums)):
            if target == nums[i]:
                output = i
                break

        return output

        
# @lc code=end


