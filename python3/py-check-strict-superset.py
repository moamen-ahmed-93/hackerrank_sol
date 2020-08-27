# Enter your code here. Read input from STDIN. Print output to STDOUT
setA=set(map(int,input().split()))
setn=[set(map(int,input().split())) for _ in range(int(input()))]
flag=1
# print("".join("True" else "False" if for i in range(len(setn)) ))
for i in range(len(setn)):
    if not setn[i].issubset(setA):
        print("False")
        flag=0
        break
if flag==1:
    print("True")
