#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#


def flippingBits(n):
    # Write your code here
    unsigned_n = n + 2**32
    bit_n = format(unsigned_n, 'b')
    bit_arr = list(bit_n)
    flipped_bit_arr = bit_arr

    for i in range(len(bit_arr)):
        if int(bit_arr[i]) == 0:
            flipped_bit_arr[i] = 1
        else:
            flipped_bit_arr[i] = 0

    flipped_bit_n = "".join(map(str, flipped_bit_arr))
    flipped_n = int(flipped_bit_n, 2)

    return flipped_n


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
