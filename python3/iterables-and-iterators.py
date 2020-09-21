# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
_,let,k=input(),[i for i in input().split()],int(input())

tuples=list(combinations(let,k))
num=0
#print(tuples)
for i in tuples:
    #print(i[0])
    if 'a' in i:
        num+=1
print(num/len(tuples))
