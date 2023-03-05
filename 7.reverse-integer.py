#
# @lc app=leetcode id=7 lang=python
#
# [7] Reverse Integer
#

# @lc code=start
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        rev_x = ''
        sign = 1 if x > 0 else -1
        x *= sign
        while x > 0:
            rev_x += str(x % 10)
            x = x//10
        x = int(rev_x)
        x *= sign
        return x if x >= -(2**31) and x <= (2**31 - 1) else 0

# @lc code=end
