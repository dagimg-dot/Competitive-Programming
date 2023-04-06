#
# @lc app=leetcode id=1859 lang=python3
#
# [1859] Sorting the Sentence
#

# @lc code=start
class Solution:
    def sortSentence(self, s: str) -> str:
        split = s.split(" ")
        num = list(map(int,[word[-1] for word in split]))
        num_old = num[:] 
        num.sort()
        final = []
        for i in range(len(num_old)):
            ix = num_old.index(num[i])
            final.append(split[ix][:-1])

        return " ".join(final)
        
# @lc code=end

