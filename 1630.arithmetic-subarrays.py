from typing import List
#
# @lc app=leetcode id=1630 lang=python3
#
# [1630] Arithmetic Subarrays
#

# @lc code=start
class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        final = []
        for i in range(len(l)):
            sub_array = nums[l[i]:r[i]+1]
            sub_array.sort()
            difference = sub_array[1] - sub_array[0]
            for j in range(1,len(sub_array)):
                if sub_array[j] != sub_array[j-1] + difference: 
                    final.append(False)
                    break
                else:
                    if j == len(sub_array) - 1:
                        final.append(True)

        return final
# @lc code=end

