#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
swaps=0
for i in range(n):
    for j in range(n-1):
        if a[j]>a[j+1]:
            temp=a[j]
            a[j]=a[j+1]
            a[j+1]=temp
            swaps+=1
print("Array is sorted in {0} swaps.".format(swaps))
print("First Element: {0}".format(a[0]))
print("Last Element: {0}".format(a[-1]))
