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

# The steps I took to solve this problem:
# 1. I checked if the input is 0 and returned 0.
# 2. I checked the sign of the input and stored it in a variable.
# 3. I converted the input to a positive number.
# 4. I set up a while loop that runs until the input is 0.
# 5. I added the last digit of the input to the rev_x string.
# 6. I removed the last digit of the input.
# 7. I converted the rev_x string to an integer.
# 8. I multiplied the integer by the sign.
# 9. I checked if the integer is within the range of a 32-bit integer.
# 10. I returned the integer if it is within the range, else I returned 0.

