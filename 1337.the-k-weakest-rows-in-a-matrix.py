from typing import List

#
# @lc app=leetcode id=1337 lang=python3
#
# [1337] The K Weakest Rows in a Matrix
#

# @lc code=start
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        dictr = {}
        for i,rows in enumerate(mat):
            count = 0
            for j in rows:
                if j == 1:
                    count += 1
                else: 
                    continue
            dictr[i] = count

        sorted_dict = dict(sorted(dictr.items(), key=lambda item: item[1]))
        final = list(sorted_dict.keys())[:k]

        return final

        
# @lc code=end
