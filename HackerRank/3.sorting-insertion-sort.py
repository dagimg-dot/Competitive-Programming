#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    last = arr[-1]
    for i in range(n-1,0,-1):
        if last < arr[i-1]:
            arr[i] = arr[i-1]
            output = " ".join(map(str,arr)) 
            print(output)
        else:
            arr[i] = last
            output = " ".join(map(str,arr)) 
            print(output)
            break
            
    if last < arr[0]:
        arr[0] = last
        output = " ".join(map(str,arr)) 
        print(output) 


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)


