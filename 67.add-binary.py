#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = a[::-1]
        b = b[::-1]

        if a == '0' and b == '0':
            return '0'        
        if len(a) != len(b):
            large = a if len(a) > len(b) else b
            small = a if len(a) < len(b) else b
            for i in range(len(small),len(large)):
                small += '0'
            loop_len = len(large) + 1
        else:
            large = a 
            small = b
            loop_len = len(a) + 1
        
        a_flag = 0
        result = ''
        for i in range(loop_len):
            if a_flag == 0:
                try:
                    c = int(large[i]) + int(small[i]) 
                    if c in [0,1]:
                        result += str(c)
                        a_flag = 0
                    else:
                        result += '0'
                        a_flag = 1 
                except:
                    pass
            else:
                if i < len(large):
                    c = int(large[i]) + int(small[i]) + a_flag
                    if c in [0,1]:
                        result += str(c)
                        a_flag = 0
                    elif c == 2:
                        result += '0'
                        a_flag = 1 
                    else:
                        result += '1'
                        a_flag = 1           
                else:
                    result += str(a_flag)
        
        return result[::-1]

        
# @lc code=end



