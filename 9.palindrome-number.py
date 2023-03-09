#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        isPal = False
        if x < 0:
            return isPal
        if x == int(str(x)[::-1]):
            isPal = True
        return isPal
        
# @lc code=end

