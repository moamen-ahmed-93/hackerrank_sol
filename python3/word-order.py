# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
od = OrderedDict()
N=int(input())
for i in range(N):
    s=input()
    if s in od:
        od[s]+=1
    else:
        od[s]=1
print(len(od.keys()))
print(*od.values())
