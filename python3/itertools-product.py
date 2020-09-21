# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product
#a,b=(int(i) for i in input().split()),set(int(i) for i in input().split())
print(" ".join(str(i) for i in list(product([int(i) for i in input().split()],[int(i) for i in input().split()]))))
