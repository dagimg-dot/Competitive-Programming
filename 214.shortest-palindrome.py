#
# @lc app=leetcode id=214 lang=python3
#
# [214] Shortest Palindrome
#

# @lc code=start
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        s_old = s
        s = s[::-1] 
        i = 1
        while s != s[::-1]:
            s = s_old[::-1]
            s = s + s[:i][::-1]
            i += 1

        return s



# @lc code=end


