# Enter your code here. Read input from STDIN. Print output to STDOUT
_,setA,_,setB=input(), set(map(int,input().split())),input(), set(map(int,input().split()))
print(len(setA.difference(setB)))
