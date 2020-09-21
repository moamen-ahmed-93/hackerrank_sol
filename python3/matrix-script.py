#!/bin/python3

import math
import os
import random
import re
import sys




first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []
count=0
turn=0
st=list(["" for i in range(m)])
for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
for i in matrix:
    turn=0
    for j in i:
        st[turn]+=j
        turn+=1
    count+=1
print(re.sub(r'(?<=\w)\W+(?=\w)',' ',"".join(i for i in st)))




