

def product(fracs):
    t =reduce(lambda f1,f2:f1*f2,fracs) # complete this line with a reduce statement
    return t.numerator, t.denominator

