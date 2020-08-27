# Enter your code here. Read input from STDIN. Print output to STDOUT

N,M=map(int,input().split())

string=""
for i in range(N//2):
    temp=".|."
    temp=temp*(2*(i+1)-1)
    print(temp.center(M,"-"))
print("WELCOME".center(M,"-"))
for i in range(N//2,0,-1):
    temp=".|."
    temp=temp*(2*(i)-1)
    print(temp.center(M,"-"))
