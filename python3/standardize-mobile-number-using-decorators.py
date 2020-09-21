def wrapper(f):
    def fun(l):
        # complete the function
        _l=list()
        for i in range(len(l)):
            
            _l.append("+91 "+l[i][-10:-5]+" "+l[i][-5:])
        return f(_l)
    return fun

