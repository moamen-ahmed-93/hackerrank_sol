from collections import OrderedDict 
def merge_the_tools(string, k):
    # your code goes here
    for i in range(len(string)//k):
        print("".join(OrderedDict.fromkeys(string[k*i:k*(i+1)])))

