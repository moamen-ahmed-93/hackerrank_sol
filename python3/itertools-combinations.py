# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
string,k=input().split()
arr=[i for i in range(1,int(k)+1)]
print("\n".join(["".join(i) for j in range(1,int(k)+1) for i in list(combinations(sorted(string),j))]))
#print(arr[i] for i in range(len(arr)))
