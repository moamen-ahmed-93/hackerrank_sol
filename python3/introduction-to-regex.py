# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
for _ in range(int(input())):    
    print("".join("True" if re.findall("^[-.+]?(\d+)?\.\d+$",input()) else "False"))
