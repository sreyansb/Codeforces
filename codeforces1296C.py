for _ in range(int(input())):
    n=int(input())
    s=input()
    li={(0,0):0}
    x,y=(0,0)
    sol=[]
    len=1000000000000
    for i in range(n):
        if s[i]=='L':
            x-=1
        elif s[i]=='R':
            x+=1
        elif s[i]=='U':
            y+=1
        else:
            y-=1
        #don't break if condition is met
        if (x,y) in li:
            len=min(len,i+1-li[(x,y)]-1)
            if len==i+1-li[(x,y)]-1:
                sol=[li[(x,y)]+1,i+1]
            #has to be i+1 and not i
            li[(x,y)]=i+1
        else:
            li[(x,y)]=i+1
    if sol:
            print(*sol)
    else:
            print(-1)


"""
for _ in range(int(input())):
    n=int(input())
    s=input()
    x,y=(0,0)
    di={}
    di[(x,y)]=0
    sol=[]
    c=n
    for i in range(0,n):
        if s[i]=='L':
            x-=1
        elif s[i]=='R':
            x+=1
        elif s[i]=='U':
            y+=1
        else:
            y-=1
        if (x,y) in di:
            b=i-di[(x,y)]
            if b<c:
                c=b
                sol=[di[(x,y)]+1,i+1]
        di[(x,y)]=i+1
    if sol:
        print(*sol)
    else:
        print(-1)
"""      
        
                
            
    
        
                
    
        
            
        
