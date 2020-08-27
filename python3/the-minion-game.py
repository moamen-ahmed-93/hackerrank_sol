def minion_game(s):
    # your code goes here
    vowels='AEIOU'
    stuart=0
    kevin=0
    for i in range(len(s)):
        if s[i] in vowels:
            kevin += len(s)-i
        else:
            stuart += len(s)-i
    if kevin > stuart:
        print("Kevin "+str(kevin))
    elif stuart>kevin:
        print("Stuart "+str(stuart))
    else:
        print("Draw")

