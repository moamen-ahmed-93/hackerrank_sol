# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
string,k=input().split()
print(*["".join(i) for i in list(permutations(sorted(string),int(k)))],sep="\n")
