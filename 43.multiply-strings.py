#
# @lc app=leetcode id=43 lang=python3
#
# [43] Multiply Strings
#

# @lc code=start
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1_int = 0
        num2_int = 0
        for i in range(len(num1)):
            num1_int = num1_int*10 + (ord(num1[i]) - 48)
        for i in range(len(num2)):
            num2_int = num2_int*10 + (ord(num2[i]) - 48)

        return str(num1_int*num2_int)
        

        
# @lc code=end



