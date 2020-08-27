def swap_case(s):
    swaped=""
    for i in s:
        if i.islower():
            swaped=swaped+i.upper()
        elif i.isupper():
            swaped=swaped+i.lower()
        else:
            swaped=swaped+i
    return swaped

