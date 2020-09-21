# Enter your code here. Read input from STDIN. Print output to STDOUT
import re 
r = re.search(r'([a-zA-Z0-9])\1+',input())
print(r.group(1) if r else -1)
