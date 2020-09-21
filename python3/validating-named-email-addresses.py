# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
for _ in range(int(input())):
    name,mail = input().split()
    x = re.findall("^<[a-zA-Z][.a-zA-Z0-9_-]*@[a-zA-Z]+\.[a-zA-Z]{1,3}>", mail)
    if len(x)!=0:
        print(name , x[0])
