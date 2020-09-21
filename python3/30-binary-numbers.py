#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
b=str(bin(n))[2:]
maxN=0
temp=1
for i in range(1,len(b)):
    if b[i]==b[i-1]:
        temp+=1
    else:
        temp=1
    if temp>maxN:
            maxN=temp
print(maxN)
