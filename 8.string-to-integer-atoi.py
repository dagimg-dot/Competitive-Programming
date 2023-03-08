#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        sign = 1
        s = s.strip()
        if len(s) == 0:
            return 0
        if s[0] in ['-', '+']: 
            if s[0] == '-':
                s = s[1:]   
                sign = -1
            elif s[0] == '+':
                s = s[1:]

        integer = 0
        for i in range(len(s)):
            if s[i].isdigit():
                integer = integer*10 + int(s[i])
            else:
                break
        final = integer*sign
        if final <= -(2**31):
            return -(2**31)
        elif final >= (2**31 - 1):  
            return (2**31 - 1)
        else:
            return final
# @lc code=end

