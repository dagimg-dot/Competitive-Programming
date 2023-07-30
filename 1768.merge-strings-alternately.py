#
# @lc app=leetcode id=1768 lang=python3
#
# [1768] Merge Strings Alternately
#

# @lc code=start
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ''

        shorter =  word2 if len(word1) > len(word2) else word1
        longer = word2 if len(word1) < len(word2) else word1

        for i in range(len(shorter)): 
            merged += word1[i]
            merged += word2[i]

        merged += longer[len(shorter):]

        return merged 
# @lc code=end

