#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip() 
        while s.find(' ') != -1:
            s = s[s.find(' ') + 1:]
        return len(s)

# @lc code=end