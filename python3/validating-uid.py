# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

def verify(s):
    if len(s)!=10:
        return False
    if not s.isalnum():
        return False
    if len(re.findall(r'\d',s))<3:
        return False
    if len(re.findall(r'[A-Z]',s))<2:
        return False
    if len(re.findall(r'.*(\w).*\1',s))>0:
        return False
    return True
    

for _ in range(int(input())):
    s=input()
    print("Valid" if verify(s) else "Invalid")
