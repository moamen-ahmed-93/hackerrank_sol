import numpy

N,M =map(int,input().split())

arr=numpy.array([input().split() for _ in range(N)],dtype=int)
print(numpy.transpose(arr))
print(arr.flatten())
