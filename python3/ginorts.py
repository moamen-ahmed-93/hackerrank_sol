# Enter your code here. Read input from STDIN. Print output to STDOUT

print(*sorted(input(),key=lambda x:(x.isdigit(),x.isdigit() and int(x)%2==0,x.isupper(),x.islower(),x)),sep='')
