# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n = int(input())
for _ in range(n):
    if re.match(r'^[789]\d{9}$',input())!=None:
        print("YES")
    else:
        print("NO")
