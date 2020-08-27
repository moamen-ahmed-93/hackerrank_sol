import numpy

N,M=map(int,input().split())
x=list()
for j in range(N):
    temp=numpy.array([int(i) for i in input().split()])
    x.append(temp)
print(numpy.prod(numpy.sum(x,axis=0)))
