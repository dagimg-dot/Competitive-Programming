#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    valley = 0
    countD = 0
    for step in path:
        if step == 'D':
          countD += 1
        else:
           countD -= 1  
           if countD == 0:
              valley += 1

    return valley

    





x = countingValleys(12,'DDUUUUDDUDD')
print(x)
