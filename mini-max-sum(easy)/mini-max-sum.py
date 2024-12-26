#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def miniMaxSum(arr):
    # Write your code here
    min_num = min(arr)
    max_num = max(arr)
    max_sum = 0
    min_sum = 0
    count = 0

    for i in arr:
        if i == min_num:
            count = count + 1

    if count != len(arr):
        for i in arr:
            if i != min_num:
                max_sum = max_sum + i

            if i != max_num:
                min_sum = min_sum + i
    else:
        min_sum = min_num * (len(arr) - 1)
        max_sum = min_sum

    print(f"{min_sum} {max_sum}")


if __name__ == "__main__":

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
