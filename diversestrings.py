t=int(input())
l=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for j in range (t):
    s=input()
    s=sorted(list(s))
    flag=0
    if len(s)==1:
        print("YES")
        flag=1
    elif len(s)==len(set(s)):
        k=1
        prev=s[0]
        while(flag==0 and k<len(s)):
            i=s[k]
            if abs(l.index(prev)-l.index(i))!=1:
                flag=1
            k+=1
            prev=i
        if flag==0:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
                
            
            
        
        
    
      
