from typing import List
#
# @lc app=leetcode id=969 lang=python3
#
# [969] Pancake Sorting
#

# @lc code=start
class Solution:
    def select(self, arr, upto):
        max = 0
        for i in range(upto + 1):
            if arr[i] > arr[max]:
                max = i
                
        return max
    
    def reverse(self,arr,start,end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start+=1
            end-=1 

        return arr

    def pancakeSort(self, arr: List[int]) -> List[int]:
        flips = []
        for i in range(len(arr)):
            upto = len(arr) - (i + 1)
            max  = self.select(arr,upto)
            flips.append(max + 1)
            flips.append(upto + 1)
            arr = self.reverse(arr,0,max)
            arr = self.reverse(arr,0,upto)
        
        return flips
        
# @lc code=end

# Steps I took to solve the problem:
# 1. Find the max element in the array
# 2. Flip the array from 0 to max
# 3. Flip the array from 0 to the position of the max element
# 4. Repeat the above steps for the remaining elements in the array

