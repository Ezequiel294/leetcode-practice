#!/bin/python3

import math
import os
import random
import re
import string
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#


def alph_shift(k, alph):
    size_alph = len(alph)
    sft_alph = [""] * size_alph

    for i in range(size_alph):
        sft_alph[(i - k) % size_alph] = alph[i]

    return sft_alph


def caesarCipher(s, k):
    # Write your code here
    alph = list(string.ascii_lowercase)
    sft_alph = alph_shift(k, alph)
    s_arr = list(s)

    for i in range(len(s_arr)):
        if s_arr[i].isalpha():
            if s_arr[i].isupper():
                s_arr[i] = s_arr[i].lower()
                s_arr[i] = sft_alph[alph.index(s_arr[i])].upper()
            else:
                s_arr[i] = sft_alph[alph.index(s_arr[i])]

    return "".join(s_arr)


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + "\n")

    fptr.close()
