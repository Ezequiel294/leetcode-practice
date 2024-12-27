#!/bin/python3

import math
import os
import random
import re
import sys
import string

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def pangrams(s):
    # Write your code here
    letters_arr = list(string.ascii_lowercase + ' ')
    freq_arr = [0] * len(letters_arr)
    arr_s = list(s)

    for i in range(len(arr_s)):
        arr_s[i] = arr_s[i].lower()

    for i in range(len(letters_arr)):
        if letters_arr[i] in arr_s:
            freq_arr[i] += 1

    if 0 in freq_arr:
        return "not pangram"
    else:
        return "pangram"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
