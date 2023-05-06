from typing import List
#
# @lc app=leetcode id=1877 lang=python3
#
# [1877] Minimize Maximum Pair Sum in Array
#

# @lc code=start
class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        first =  nums[0] + nums[-1]
        l = 1
        r = len(nums) - 2
        while l < r:
            if nums[l] + nums[r] > first:
                first = nums[l] + nums[r]
            l += 1
            r -= 1

        return first
    
# @lc code=end

# Steps I took to solve this problem:
# 1. Sort the list in ascending order
# 2. Find the sum of the first and last element in the list
# 3. Find the sum of the second and second last element in the list
# 4. Compare the sum of the first and last element with the sum of the second and second last element
# 5. If the sum of the second and second last element is greater than the sum of the first and last element, then the sum of the second and second last element is the new sum of the first and last element
# 6. Repeat steps 3 to 5 until the sum of the second and second last element is less than the sum of the first and last element
# 7. Return the sum of the first and last element