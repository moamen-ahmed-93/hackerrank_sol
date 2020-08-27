# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m=map(int,input().split())
happy=0

array=[i for i in input().split()]
setA=set([i for i in input().split()])
setB=set([i for i in input().split()])


for i in array:
    if i in setA:
        happy+=1
    if i in setB:
        happy-=1
print(happy)
