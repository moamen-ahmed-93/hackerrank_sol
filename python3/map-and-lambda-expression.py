cube = lambda x:x**3 # complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    if n==1:
        return [0]
    if n==0:
        return []
    fib=list()
    f1=0
    f2=1
    fib.append(f1)
    fib.append(f2)
    for i in range(n-2):
        f3=f2
        f2=f1+f2
        f1=f3
        fib.append(f2)
    return fib
