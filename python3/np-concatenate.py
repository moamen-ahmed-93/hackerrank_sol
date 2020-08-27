import numpy



N,M,P = map(int,input().split())

arr1=numpy.array([input().split() for _ in range(N)],dtype=numpy.int)
arr2=numpy.array([input().split() for _ in range(M)],dtype=numpy.int)

print(numpy.concatenate((arr1,arr2),axis = 0))
