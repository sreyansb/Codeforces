s=input()
k=s.find("AB")
j=s.find("BA")
m=min(k,j)
if m==-1:
    print("NO")
else:
    flag=1
    if m==k:
        b=s[m+2:].find("BA")
        if b!=-1:
            print("YES")
        else:
            flag=0
    else:
        b=s[m+2:].find("AB")
        if b!=-1:
            print("YES")
        else:
            flag=0
    if flag==0:
        if s.count("AB")>1 or s.count("BA")>1:
            if s.count("AB")>1:
                if s[j+2:].find("AB")!=-1:
                    print("YES")
                else:
                    print("NO")
            elif s.count("BA")>1:
                if s[k+2:].find("BA")!=-1:
                    print("YES")
                else:
                    print("NO")
        else:
            print("NO")
        
            
    
