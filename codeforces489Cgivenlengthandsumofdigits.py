m,s=map(int,input().split())
if s<1 or s>m*9:
    print("-1 -1")
else:
    k='9'*(m-1)
    if k==0:
        k=""
    if len(str(s))==1:
        minu=str(max(int(str(s-9*(m-1))+str(k)),int(str(s)+(m-1)*'0')))
    else:
        minu=str(s-9*(m-1))+str(k)
    maxu=list(minu)
    minco=list(minu)
    if len(minu)<=1:
        maxu=minu
    else:
        for i in range(1,len(minco)):
            if int(minco[i-1])+int(minco[i])<10:
                maxu[i-1]=str(int(minco[i-1])+int(minco[i]))
                minco[i]='0'
            else:
                minco[i]=str(int(minco[i-1])+int(minco[i])-9)
                maxu[i-1]='9'
        maxu[-1]=minco[-1]
    maxu="".join(maxu)
    print(minu,maxu)
                
                
                
                
        
        
    
        
