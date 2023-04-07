from typing import List
#
# @lc app=leetcode id=1985 lang=python3
#
# [1985] Find the Kth Largest Integer in the Array
#

# @lc code=start
class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums = list(map(int,nums))
        nums.sort()
        return str(nums[-k])
        
# @lc code=end

# steps i took to solve this problem:
# 1. I converted the list of strings to a list of integers.
# 2. I sorted the list.
# 3. I returned the kth largest element in the list by using negative indexing.




