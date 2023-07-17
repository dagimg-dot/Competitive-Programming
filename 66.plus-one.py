from typing import List
#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits.reverse()


        for i in range(len(digits)):
            digits[i] = digits[i] + 1
            if digits[i] > 9:
                digits[i] = 0
                if i + 1 == len(digits):           
                    digits.append(1)
                    digits.reverse()
                    return digits
                continue
            else:
                digits.reverse()
                return digits

        
# @lc code=end

