# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

n=int(input())
for _ in range(n):
    for j in re.findall(r'((?!^)\#([0-9A-Fa-f]{3})([0-9A-Fa-f]{3})?)',input()):
        print(j[0])
