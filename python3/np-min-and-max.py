import numpy as np

N,M = map(int,input().split())
x=np.array([input().split() for _ in range(N)],dtype=np.int)
print(np.max(np.min(x,axis=1)))
