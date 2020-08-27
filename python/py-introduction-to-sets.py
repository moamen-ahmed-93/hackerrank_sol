

def average(array):
    # your code goes here
    s=set(array)
    avg=0
    for i in s:
        avg+=i
    return avg/len(s)

