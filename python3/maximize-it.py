# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product
K,M=map(int,input().split())

arr=[[int(i)**2 for i in input().split()[1:]] for _ in range(K)]
#print(arr)
co=list(set(product(*arr)))
print(max(sum(j) % M for j in co))
