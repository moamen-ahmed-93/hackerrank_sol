# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
def rep(match):
    if match.group(0) == '&&':
        return 'and'
    if match.group(0) == '||':
        return 'or'
n=int(input())
for _ in range(n):
    print(re.sub(r'(?<=\s)\&\&(?=\s)||(?<=\s)\|\|(?=\s)',rep,input()))
