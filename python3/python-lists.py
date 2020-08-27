if __name__ == '__main__':
    N = int(input())
    output=[]
    for _ in range(N):
        line=list(input().split(" "))
        if line[0] == "insert":
            # print(line[0])
            # output[int(line.insert(1,int(line[2]))]
            output.insert(int(line[1]),int(line[2]))
        elif line[0] == "print":
            print(output)
        elif line[0] == "remove":
            output.remove(int(line[1]))
        elif line[0] == "append":
            output.append(int(line[1]))
        elif line[0] == "sort":
            output.sort()
        elif line[0] == "pop":
            output.pop()
        elif line[0] == "reverse":
            output.reverse() 
