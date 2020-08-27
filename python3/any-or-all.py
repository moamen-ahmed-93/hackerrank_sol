# Enter your code here. Read input from STDIN. Print output to STDOUT
n=input()
arr = list(map(int, input().split()))
print(all([all(True if i >0 else False for i in arr),any(i for i in arr if str(i) == str(i)[::-1])]))
