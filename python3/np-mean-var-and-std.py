import numpy as np

np.set_printoptions(legacy='1.13')

N,M = map(int,input().split())
x=np.array([input().split() for _ in range(N)],dtype=np.int)
print(np.mean(x,axis=1))
print(np.var(x,axis=0))
print(np.std(x))
