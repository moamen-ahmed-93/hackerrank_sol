# Enter your code here. Read input from STDIN. Print output to STDOUT
n,x=map(int,input().split())
sub=list()
for _ in range(x):
    sub.append([float(i) for i in input().split()])
print("\n".join(str(sum([sub[i][j] for i in range(x)])/x) for j in range(n)))
