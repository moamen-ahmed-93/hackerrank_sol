# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
d = deque()
N=int(input())
for _ in range(N):
    s=input().split()
    #print(s)
    if s[0].find("append")!=-1:
        getattr(d,s[0])(int(s[1]))
    else:
        getattr(d,s[0])()
print(*d)
