for _ in range(int(input())):
    s=input()
    n=len(s)
    k=set(s)
    """if len(k)==1:
        if k=={'L'}:
            print(n+1)
        elif k=={'R'}:
            print("1")
    else:
        k=s.find("R")
        if k==n-1:
            print(n)
        else:
            if s[k+1]=="L":
                print(k+2)
            else:
                print(k+1)"""
    leftpos=0
    rightpos=0
    for i in range(n):
        if s[i]=='L':
            leftpos=i+1
        elif s[i]=='R' and rightpos==0:
            righpos=i+1
    
