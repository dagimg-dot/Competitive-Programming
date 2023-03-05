#
# @lc app=leetcode id=13 lang=python
#
# [13] Roman to Integer
#

# @lc code=start
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}     
        int = 0
        i = 0
        loop_length = len(s)
        while i < loop_length:
            exception = 0
            if i != loop_length - 1:
                if s[i] in ['I','X','C'] and s[i + 1] in list(roman.keys()) and roman[s[i + 1]] > roman[s[i]]:
                    exception = roman[s[i + 1]] - roman[s[i]]
                    int += exception
                    i += 1  
                else:
                    int += roman[s[i]]
            else:
                int += roman[s[i]]
            i += 1
        
        return int
        
# @lc code=end

