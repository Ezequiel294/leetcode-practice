#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#


def sockMerchant(n, ar):
    # Write your code here
    pair_count = 0
    ar.sort()
    i = 0
    j = 0

    while i < n:
        match_count = 1
        j = i + 1
        while j < n:
            if ar[i] == ar[j]:
                match_count += 1
                j += 1
            else:
                break
        pair_count += int(match_count/2)
        i = j

    return pair_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
