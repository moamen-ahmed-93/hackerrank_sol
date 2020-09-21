#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    s=list()
    for i in range(0,4):
        for j in range(1,5):
            s.append(arr[i][j]+arr[i][j+1]+arr[i][j-1]+arr[i+1][j]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j-1])
    return max(s)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
