#
# @lc app=leetcode id=357 lang=python3
#
# [357] Count Numbers with Unique Digits
#
# @lc code=start
class Solution:
    def count_not_unique(self,n:int) -> int:
        not_unique = 0
        for i in range(10**(n-1),2*10**(n-1)):
            str_i = str(i)
            for i in range(len(str_i)):
                if str_i[i] in str_i[i+1:]:
                    not_unique += 1
                    break

        return not_unique
    
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        not_unique = 0
        old_n = n
        if n == 0:
            return 1
        if n == 1:
            return 10
        while n > 1:
            pattern = self.count_not_unique(n)
            not_unique += 9 * pattern
            n -= 1

        return 10**old_n - not_unique
        
# @lc code=end






