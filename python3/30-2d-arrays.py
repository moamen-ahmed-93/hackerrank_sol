#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    arr = list()
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    #print(arr)
    maxN=-1000
    for i in range(1,5):
        for j in range(1,5):
            temp=arr[i-1][j-1]+arr[i-1][j]+arr[i-1][j+1]+arr[i][j]+arr[i+1][j-1]+arr[i+1][j]+arr[i+1][j+1]
            if temp > maxN:
                maxN=temp
    print(maxN)
