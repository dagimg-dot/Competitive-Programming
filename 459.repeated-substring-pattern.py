#
# @lc app=leetcode id=459 lang=python3
#
# [459] Repeated Substring Pattern
#

# @lc code=start
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        factors = []
        if len(s) == 1:
            return False

        for i in range(1,len(s)):
            if len(s) % i == 0:
                factors.append(i)

        for fact in factors:
            t = s[:fact] * (len(s)//fact)
            if t == s:
                return True
        

        return False

# @lc code=end
