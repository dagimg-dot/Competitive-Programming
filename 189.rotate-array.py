from typing import List

#
# @lc app=leetcode id=189 lang=python3
#
# [189] Rotate Array
#

# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        if k == 0:
            pass
        else:
            for i in range(k):
                nums.insert(0, nums.pop())

        
# @lc code=end

