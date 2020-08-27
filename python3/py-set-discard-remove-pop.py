n = int(input())
s = set(map(int, input().split()))
m= int(input())
for _ in range(m):
    x=input().split()
    if x[0] == "pop":
        s.pop()
    elif x[0] == "remove":
        if int(x[1]) in s:
            s.remove(int(x[1]))
    elif x[0] == "discard":
        s.discard(int(x[1]))
print(sum(s))
