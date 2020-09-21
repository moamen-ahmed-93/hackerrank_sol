# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
od = OrderedDict()
N = int(input())
for i in range(N):
    item=input().rpartition(" ")
    if item[0] in od.keys():
        od[item[0]]+=int(item[-1])
    else:
        od[item[0]]=int(item[-1])
print("\n".join(key+" "+str(od[key]) for key in od))
