# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
r = list(re.finditer(r'([QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm]?)([AEIOUaeiou]{2,})([QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])',input()))

if len(r)<=0:
    print(-1)
else:
    for i in r:
        print(i.group(2))
