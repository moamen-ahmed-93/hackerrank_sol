# Enter your code here. Read input from STDIN. Print output to STDOUT
for _ in range(int(input())):
    s=input()
    s1="".join(s[i] for i in range(0,len(s),2))
    s2="".join(s[i] for i in range(1,len(s),2))
    print(str(s1),str(s2))
