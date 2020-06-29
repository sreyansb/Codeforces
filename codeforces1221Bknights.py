import math
n=int(input())
a=[[0 for i in range (n)]for j in range(n)]

for i in range(n):
    if i%2:
        ch='B'
    else:
        ch='W'
    for j in range(n):
        print(ch,end="")
        if ch=="W":
            ch='B'
        else:
            ch="W"
    print()
            
        
