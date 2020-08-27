def print_rangoli(n):
    # your code goes here
    width=4*n-3
    # print(width)
    for i in range(n):
        #print(i)
        # print(chr(i+ord('a')))
        string="-".join([chr(z+ord('a')) for z in range(n-i-1,n)])
        string=string[::-1]+string[1:]
        print(string.center(width,'-'))
    for i in range(n-2,-1,-1):
        string="-".join([chr(z+ord('a')) for z in range(n-i-1,n)])
        string=string[::-1]+string[1:]
        print(string.center(width,'-'))

