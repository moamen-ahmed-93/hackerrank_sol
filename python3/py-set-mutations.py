# Enter your code here. Read input from STDIN. Print output to STDOUT
_,setA=input(),set(map(int,input().split()))
# print(setA)
for _ in range(int(input())):
    command=input().split()
    if command[0]=="intersection_update":
        setA.intersection_update(set(int(i) for i in input().split()))
        #print(setA)
    if command[0]=="symmetric_difference_update":
        setA.symmetric_difference_update(set(int(i) for i in input().split()))
        #print(setA)
    if command[0]=="difference_update":
        setA.difference_update(set(int(i) for i in input().split()))
        #print(setA)
    if command[0]=="update":
        setA.update(set(int(i) for i in input().split()))
print(sum(setA))
