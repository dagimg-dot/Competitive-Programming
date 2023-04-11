from typing import List
#
# @lc app=leetcode id=2007 lang=python3
#
# [2007] Find Original Array From Doubled Array
#

# @lc code=start
class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed.sort() # 1,2,3,4,6,8
        zeros = changed.count(0)
        final = []
        if zeros % 2 == 0:
            final = [0] * (zeros // 2)
            if zeros != len(changed):
                changed = changed[zeros:]
            else:
                return final
        else:
            return []
        
        counts = {}
        for elt in changed:
            if elt in counts:
                counts[elt] += 1
            else:
                counts[elt] = 1

        for elt in counts:
            if counts[elt] > 0 and elt*2 in counts and counts[elt*2] > 0:
                pairs = min(counts[elt], counts[elt*2])
                final += [elt] * pairs
                counts[elt] -= pairs
                counts[elt*2] -= pairs

        for elt in counts:
            if counts[elt] != 0:
                return []

        return final

# @lc code=end

# Steps I took to solve this problem:

# 1. Sort the array
# 2. Count the number of zeros
# 3. If the number of zeros is even, add half of them to the final array
# 4. If the number of zeros is odd, return an empty array
# 5. If the number of zeros is not equal to the length of the array, start the changed array at the index of the first non-zero element
# 6. Create a dictionary to store the counts of each element
# 7. Iterate through the dictionary
# 8. If the count of the current element is greater than 0 and the count of the current element times 2 is greater than 0, add the minimum of the two counts to the final array
# 9. Subtract the minimum of the two counts from the counts of the current element and the current element times 2
# 10. If the count of the current element is not equal to 0, return an empty array  
# 11. Return the final array






