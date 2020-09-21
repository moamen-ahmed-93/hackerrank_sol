#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    numofa=0
    final=0
    for i in s:
        if i == 'a':
            numofa+=1
    reps=n//len(s)
    extra=n%len(s)
    final=reps*numofa
    for i in range(extra):
        if s[i]=='a':
            final+=1
    return final

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
