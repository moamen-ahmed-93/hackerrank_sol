# Enter your code here. Read input from STDIN. Print output to STDOUT
m=int(input())
setA=set(int(i) for i in input().split())
n=int(input())
setB=set(int(i) for i in input().split())
print("\n".join( str(i) for i in sorted(list(setA.difference(setB).union(setB.difference(setA))))))
