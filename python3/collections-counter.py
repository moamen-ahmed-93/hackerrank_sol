# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
n,shoes=input(),[int(i) for i in input().split()]
x=dict()
c=Counter(shoes).items()
#print(Counter(shoes).items())
for i,j in c:
    x[i]=j
n=int(input())
money=0
for i in range(n):
    size,price=map(int,input().split())
    if size in x.keys() and x[size]!=0:
        x[size]-=1
        money+=price
print(money)
