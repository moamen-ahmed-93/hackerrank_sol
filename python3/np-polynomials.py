import numpy

n = list(map(float,input().split()));
m = input();
print(numpy.polyval(n,int(m)));

