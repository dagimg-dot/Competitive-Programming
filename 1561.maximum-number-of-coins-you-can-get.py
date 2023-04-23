from typing import List
#
# @lc app=leetcode id=1561 lang=python3
#
# [1561] Maximum Number of Coins You Can Get
#

# @lc code=start
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        count = []
        third = len(piles) / 3
        for i in range(1,len(piles),2):
            if len(count) <= third - 1: 
                count.append(piles[i])
            else:
                break


        return sum(count)
        


           
# @lc code=end

# Steps I took to solve this problem
# 1. Sort the list in descending order
# 2. Create a list to store the values of the second element in the list
# 3. Loop through the list and add the second element to the list if the length of the list is less than or equal to the third of the length of the list
# 4. Return the sum of the list

