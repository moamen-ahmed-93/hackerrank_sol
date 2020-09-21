# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import groupby

s=input()

print(*[(len(list(j)),int(i)) for i,j in groupby(s) ])
