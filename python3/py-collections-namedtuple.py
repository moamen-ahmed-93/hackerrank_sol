# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple
Grades = namedtuple('Grades','ID NAME CLASS MARKS')
N=int(input())
col=input().split()
avg=0
for i in range(N):
    row=input().split()
    avg+=int(row[col.index('MARKS')])

print(avg/N)
