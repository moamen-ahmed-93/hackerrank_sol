#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    steps=0
    i=0
    while True:
        if i>=len(c)-1:
            break
        elif (i+2)<len(c) and c[i+2]==0: 
            steps+=1
            i+=2
        elif c[i+1]==0:
            steps+=1
            i+=1
    return steps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
