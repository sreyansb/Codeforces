li=list(map(int,input().split()))
li.sort()
s=set(li)
if len(s)==1:
    print("Elephant")
elif len(s)==2:
    flag=0
    for i in s:
        if li.count(i)>3:
            flag=i
            break
    if flag:
        for i in s:
            if i!=flag:
                if li.count(i)==1:
                    print("Bear")
                else:
                    print("Elephant")
    else:
        print("Alien")
elif len(s)==3:
    flag=0
    for i in s:
        if li.count(i)==4:
            flag=i
            s.remove(flag)
            break
    if flag:
        s=list(s)
        if s[0]>s[1] or s[1]>s[0]:
            print("Bear")
        elif s[0]==s[1]:
            print("Elephant")
        else:
            print("Alien")
    else:
        print("Alien")
else:
    print("Alien")
    
                
        
    
