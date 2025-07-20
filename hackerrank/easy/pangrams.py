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
    arr_s = list(s)

    for i in range(len(arr_s)):
        arr_s[i] = arr_s[i].lower()

    for letter in letters_arr:
        if letter not in arr_s:
            return "not pangram"

    return "pangram"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
