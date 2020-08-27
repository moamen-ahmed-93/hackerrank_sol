import numpy as np

N=int(input())

a=np.array([input().split() for _ in range(N)],dtype=np.int)
b=np.array([input().split() for _ in range(N)],dtype=np.int)
# ans=np.array([[np.dot(a,b)],[np.cross(a,b)]],dtype=int)
print(np.dot(a,b))
