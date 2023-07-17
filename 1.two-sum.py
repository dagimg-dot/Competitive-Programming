#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # for i in range(len(nums)):
        #     # print(f"I ran {i} times")
        #     for j in range(len(nums)):
        #         print(f"I ran {i + j} times")
        #         if i!=j and nums[i] + nums[j] == target:
        #             return [i,j]

        dict = {}
        for i,num in enumerate(nums):
            if target - num in dict:
                return [dict[target - num],i]
            else:
                dict[num] = i

# @lc code=end

# The steps I took to solve this problem:
# 1. I set up a nested for loop that runs through the elements of nums list.
# 2. It returns the first occurrence where the elements add up to a target.
# 3. It ignores the case where both the elements to add are equal.
        
# The optimal solution, I came across, was to use a dictionary.

# 1. We create a dictionary.
# 2. We iterate through the elements of the nums list.
# 3. We check if the difference between the target and the element is in the dictionary.
# 4. If it is, we return the index of the difference and the current index.
# 5. If it is not, we add the element to the dictionary.
# 6. We repeat the process until we find the first occurrence where the elements add up to a target.
