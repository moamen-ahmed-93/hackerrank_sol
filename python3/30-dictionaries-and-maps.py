# Enter your code here. Read input from STDIN. Print output to STDOUT
d=dict()
for _ in range(int(input())):
    name,number=input().split()
    d[name]=number
    

while True:
    try:
        s = input()
    except:
        break
    print(s+"="+d[s] if s in d.keys() else "Not found")
