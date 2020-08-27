# Enter your code here. Read input from STDIN. Print output to STDOUT
k,arr=int(input()),sorted(list(map(int,input().split())))
# print("".join(str(i) for i in set(arr) if len(arr.count(i)==1))
for i in range(0,len(arr),k):
    if (i+k-1) > len(arr) or arr[i]!=arr[i+k-1]:
        print(arr[i])
        break
