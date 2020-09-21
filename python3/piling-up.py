# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
for _ in range(int(input())):
    n=int(input())
    d=deque([int(i) for i in input().split()])
    for i in reversed(sorted(d)):
        if i == d[0]:
            d.popleft()
        elif i == d[-1]:
            d.pop()
        else:
            break
    if len(d)==0:
        print("Yes")
    else:
        print("No")
