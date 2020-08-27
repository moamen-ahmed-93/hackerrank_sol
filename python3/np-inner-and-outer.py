import numpy

x=numpy.array([int(i) for i in input().split()])
y=numpy.array([int(i) for i in input().split()])

print(numpy.inner(x,y))
print(numpy.outer(x,y))
