# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
val_card=r'^([456]\d{3})(-?)(\d{4})\2(\d{4})\2(\d{4})$'
val_repeat=r'(\d)\1{3,}'
for _ in range(int(input())):
    s=input()
    x=re.findall(val_repeat,s.replace("-",""))
    #print(x)
    if len(x)>0:
        print("Invalid")
    else:
        x=re.findall(val_card,s)
        print("Valid" if len(x)>0 else "Invalid")
