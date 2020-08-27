def count_substring(string, sub_string):
    x=0
    for i in range(len(string)-len(sub_string)+1):
        if sub_string==string[i:i+len(sub_string)] :
            x=x+1
    return x

