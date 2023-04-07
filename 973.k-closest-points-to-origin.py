from typing import List
#
# @lc app=leetcode id=973 lang=python3
#
# [973] K Closest Points to Origin
#

# @lc code=start
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if len(points) == k:
            return points 

        final = {}
        for i in range(len(points)):
            distance = points[i][0]**2 + points[i][1]**2
            final[i] = distance

        sorted_dict = dict(sorted(final.items(), key=lambda item: item[1]))

        result = []
        for item in sorted_dict.keys():
            result.append(points[item])
            
        return result[:k]
            

# @lc code=end

# The steps i took to solve this problem:

# 1. I created a dictionary to store the index of the point in the original list and the distance of the point from the origin.
# 2. I sorted the dictionary by the distance of the point from the origin.
# 3. I created a list to store the points in the order of their distance from the origin.
# 4. I returned the first k points in the list.

