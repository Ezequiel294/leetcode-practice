#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def timeConversion(s):
    # Write your code here
    s_arr = list(s)
    hour = s_arr[0] + s_arr[1]
    min = s_arr[3] + s_arr[4]
    sec = s_arr[6] + s_arr[7]
    tag = s_arr[8] + s_arr[9]

    if hour == "12" and tag == "AM":
        return "00" + ":" + min + ":" + sec

    elif hour == "12" and tag == "PM":
        return "12" + ":" + min + ":" + sec

    elif tag == "PM":
        hour = str(int(hour) + 12)
        return hour + ":" + min + ":" + sec
    else:
        return hour + ":" + min + ":" + sec


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    s = input()

    result = timeConversion(s)

    fptr.write(result + "\n")

    fptr.close()
