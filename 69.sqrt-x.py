#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        if x in [0,1]:
            return x
        for i in range(x//2+2):
            if x - i*i < 0:
                return i-1




        
# @lc code=end


