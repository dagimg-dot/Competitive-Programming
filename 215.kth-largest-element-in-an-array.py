from typing import List
#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#

# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[-k]
        
# @lc code=end

# steps i took to solve this problem:
# 1. I sorted the list.
# 2. I returned the kth largest element in the list by using negative indexing.


