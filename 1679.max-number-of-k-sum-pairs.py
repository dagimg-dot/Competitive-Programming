from typing import List
#
# @lc app=leetcode id=1679 lang=python3
#
# [1679] Max Number of K-Sum Pairs
#

# @lc code=start
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        count = 0
        l = 0
        r = len(nums) - 1
        while l < r:
            if nums[l] + nums[r] == k:
                count += 1
                l+= 1
                r -= 1
            elif nums[l] + nums[r] < k:
                l += 1
            else:
                r -= 1

        return count
# @lc code=end

# Steps I took to solve this problem:
# 1. Sort the array.
# 2. Use two pointers, one at the beginning and one at the end.
# 3. If the sum of the two pointers is equal to k, increment the count and move both pointers.
# 4. If the sum of the two pointers is less than k, move the left pointer.
# 5. If the sum of the two pointers is greater than k, move the right pointer.
# 6. Return the count.




