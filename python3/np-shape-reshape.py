import numpy

arr=numpy.array([int(i) for i in input().split()],dtype=numpy.int)
print(numpy.reshape(arr,(3,3)))
