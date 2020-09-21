# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement
string,k=input().split()
print(*["".join(i) for i in list(combinations_with_replacement(sorted(string),int(k)))],sep="\n")
