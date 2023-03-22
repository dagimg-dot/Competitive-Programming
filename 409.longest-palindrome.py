#
# @lc app=leetcode id=409 lang=python3
#
# [409] Longest Palindrome
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> int:
        hash = {}
        for i in range(len(s)):
            if s[i] not in hash.keys():
                hash[s[i]] = 1
            else:
                hash[s[i]] += 1
        keys = list(hash.values())
        freq = []
        for i in range(len(keys)):
            if keys[i] % 2 == 0:
                freq.append(keys[i]) 
            else:
                freq.append(keys[i] - 1)
                if 1 not in freq:
                    freq.append(1)

            

        return sum(freq)
                
        
# @lc code=end



