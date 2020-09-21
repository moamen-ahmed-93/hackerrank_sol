

maxdepth = 0
def depth(elem, level):
    global maxdepth
    # your code goes here
    if level+1 > maxdepth:
        maxdepth = level+1
    for e in elem:
        depth(e,level+1)

