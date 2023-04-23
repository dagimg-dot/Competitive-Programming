'''
Theatre Square in the capital city of Berland has a rectangular shape with the size n*m meters. On the occasion of the city's anniversary,
a decision was taken to pave the Square with square granite flagstones. Each flagstone is of the size a*a

What is the least number of flagstones needed to pave the Square? It's allowed to cover the surface larger than the Theatre Square,
but the Square has to be covered. It's not allowed to break the flagstones. The sides of flagstones should be parallel to the sides 
of the Square.

Input
The input contains three positive integer numbers in the first line: n, m and a (1 ≤ n, m, a ≤ 109).

Output
Write the needed number of flagstones.

Examples

input
6 6 4
output
4

'''

from math import ceil

def theatre_square():
    n,m,a = map(int,input().split())
    count = ceil(n/a) * ceil(m/a)
    print(count)

theatre_square()

# Steps to solve:
# 1. Take input
# 2. Calculate the number of flagstones needed to cover the only the length of the square by dividing the 
# length of the square by the length of the flagstone in ceil function which returns the smallest integer 
# greater than or equal to the number
# 3. Calculate the number of flagstones needed to cover the only the breadth of the square
# 4. Multiply the two values to get the total number of flagstones needed to cover the square
# 5. Print the result

