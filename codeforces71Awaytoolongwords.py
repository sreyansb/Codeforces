t=int(input())
for i in range(t):
    l=input()
    if len(l)<11:
        print(l)
    else:
        print(l[0]+str(len(l[1:-1]))+l[-1])
        
    
