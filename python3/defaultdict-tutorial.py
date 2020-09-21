# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
k,n=map(int,input().split())

A=[input() for _ in range(k)]
B=[input() for _ in range(n)]
d = defaultdict(list)
for i,l in enumerate(A):
    d[l].append(i+1)
for i in B:
    if i in A:
        print(*d[i])
    else:
        print(-1)
