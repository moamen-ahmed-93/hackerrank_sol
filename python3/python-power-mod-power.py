# Enter your code here. Read input from STDIN. Print output to STDOUT
p=[int(input()) for _ in range(3)]
print("{0}\n{1}".format(pow(p[0],p[1]),pow(*p)))
