#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

def isEven(n):
    if n % 2 == 0:
        return 1
    else:
        return 0

def pageCount(n, p):
    # Write your code here
    mid = int(n/2)

    # 1 if even, 0 if odd
    n_even = isEven(n) 
    p_even = isEven(p)

    if n_even:
        if p == 1 or p == n:
            return 0
    else:
        if p == 1 or p == n or p == n-1:
            return 0

    """
    1 2,3 4,5 6,7 mid=3.5
    1 2,3 4,5 6   mid = 3
    """

    if p <= mid:
        return int(p/2)
    else:
        if n-p == 1:
            return int((n-p)/2 + 0.5)
        else:
            return int((n-p)/2)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
