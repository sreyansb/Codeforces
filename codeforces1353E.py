for _ in range(int(input())):
    n,k=map(int,input().split())
    stri=input()
    if '1' not in stri:
        print(0)
    else:
        answer=0
        lastpos=0
        for i in range(0,n):
            if stri[i]=='1':
                if i-lastpos<=k:
                    answer+=1
                lastpos=i
            else:
                if i-lastpos>=k:
                    answer+=1
                    lastpos=i
        print(answer)
            
        
