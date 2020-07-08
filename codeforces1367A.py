for _ in range(int(input())):
    s=input()
    li=[]
    for i in range(0,len(s),2):
        li.append(s[i]+s[i+1])
    #print(li)
    mains=li[0]
    s=li[0][1]
    for i in li[1:]:
        if s==i[0]:
            mains+=i[1]
        else:
            mains+=i
        s=i[1]
    print(mains)
        
        
