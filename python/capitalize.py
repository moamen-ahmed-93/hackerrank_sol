

# Complete the solve function below.
def solve(s):
    
    return "".join([s[i].upper() if ((i==0) | (s[i-1]==' '))  else s[i] for i in range(0,len(s)) ])

