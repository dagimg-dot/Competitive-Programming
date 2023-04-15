from typing import List
#
# @lc app=leetcode id=1968 lang=python3
#
# [1968] Array With Elements Not Equal to Average of Neighbors
#

# @lc code=start


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        res = [0] * n
        for i in range(n):
            if i % 2 == 0:
                res[i] = nums[i // 2]
            else:
                res[i] = nums[n - 1 - i // 2]

        return res
# @lc code=end

# Steps I took to solve this problem:
# 1. Sort the array
# 2. Create a new array of the same size and fill it with 0s
# 3. Loop through the new array and fill it with the elements from the sorted array
# 4. If the index is even, fill it with the element from the sorted array at index i // 2
# This is because the first half of the sorted array will be the smallest elements
# 5. If the index is odd, fill it with the element from the sorted array at index n - 1 - i // 2
# This is because the second half of the sorted array will be the largest elements
# 6. Return the new array
