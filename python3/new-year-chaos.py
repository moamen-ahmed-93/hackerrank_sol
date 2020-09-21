#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    jumps=0
    tempJ=0
    for i in range(len(q)):
        if q[i]-2 > i+1:
            print("Too chaotic")
            return
        tempJ=0
        for j in range(max(q[i]-2,0),i):
            if q[j]>q[i]:
                jumps+=1
    print(jumps)
if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
