

def person_lister(f):
    def inner(people):
        # complete the function
        return [f(i) for i in sorted(people,key=lambda x:int(x[2]))]

    return inner

