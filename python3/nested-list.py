if __name__ == '__main__':
    records=list()
    names=list()
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        x=[name,score]
        records.append(x)
    # print(records)
    temp=float('inf')
    second=float('inf')
    for i in records:
        if i[1]<temp:
            second=temp
            temp=i[1]
        elif (i[1]<second) & (i[1]!=temp):
            second=i[1]
    for i in records:
        if i[1] == second:
            names.append(i[0])
    for i in sorted(names):
        print(i)
