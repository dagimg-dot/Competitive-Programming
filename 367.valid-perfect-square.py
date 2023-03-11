#
# @lc app=leetcode id=367 lang=python3
#
# [367] Valid Perfect Square
#

# @lc code=start
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num in [0,1]:
            return True
        for i in range(2,num//2+1):
            if num - i*i <= 0:
                if num == i*i :
                    return True
                else:
                    return False
# @lc code=end




