# Enter your code here. Read input from STDIN. Print output to STDOUT
for _ in range(int(input())):
    _,setA,_,setB=input(),set(map(int,input().split())),input(),set(map(int,input().split()))
    print("".join("True" if setB.union(setA)==setB else "False"))
