for _ in range(int(input())):
    n,m=map(int,input().split())
    chararr=[]
    for i in range(n):
        s=input()
        chararr.append(s)
    #print(chararr)
    flagmain=1
    finstring=list(chararr[0])
    #print("main",finstring)
    for i in range(m):
        charsaved=finstring[i]
        for j in range(26):
            finstring[i]=chr(97+j)
            #print(finstring)
            flag=True
            for k in range(n):
                counts=0
                for l in range(m):
                    if chararr[k][l]!=finstring[l]:
                        counts+=1
                if counts>1:
                    flag=False
                    break
            if flag==True:
                    print ("".join(finstring))
                    flagmain=0
                    break
        if flagmain==0:
            break
        finstring[i]=charsaved
    if flagmain:
        print (-1)
                    
                               
                
        
        
        
        
            
    
            
