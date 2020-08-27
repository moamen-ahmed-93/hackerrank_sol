import numpy

numpy.set_printoptions(legacy='1.13')

N = int(input())
arr=numpy.array([input().split() for _ in range(N)],dtype=numpy.float)
print(numpy.linalg.det(arr))
