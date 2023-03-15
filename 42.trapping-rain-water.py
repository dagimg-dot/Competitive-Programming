from typing import List
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start

class Solution:
    def trap(self, height: List[int]) -> int:
        units_trapped = 0
        max_height = height.index(max(height))

        l = 0
        r = l + 1
        while r < max_height:
            if height[l] >= height[r]:
                units_trapped += height[l] - height[r]
                r += 1
            else:
                l = r
                r += 1
        
        l = len(height) - 1
        r = l - 1
        while r > max_height:
            if height[l] >= height[r]:
                units_trapped += height[l] - height[r]
                r -= 1
            else:
                l = r
                r -= 1


        return units_trapped
        
# @lc code=end

x = Solution()
height = [0,1,0,2,1,0,1,3,2,1,2,1]
u = x.trap(height)
print(u)






