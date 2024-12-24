#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def plusMinus(arr):
    # Write your code here
    size = len(arr)
    negatives = 0
    positives = 0
    zeros = 0

    for i in arr:
        if i < 0:
            negatives = negatives + 1
        elif i > 0:
            positives = positives + 1
        else:
            zeros = zeros + 1

    positives = positives / size
    negatives = negatives / size
    zeros = zeros / size

    print(f"{positives:.6f}")
    print(f"{negatives:.6f}")
    print(f"{zeros:.6f}")


if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
