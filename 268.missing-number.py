from typing import List
#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#

# @lc code=start


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing = 0
        for item in range(len(nums)+1):
            if item not in nums:
                missing = item
                break

        return missing

# @lc code=end

