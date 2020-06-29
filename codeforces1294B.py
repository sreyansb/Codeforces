for _ in range(int(input())):
    n=int(input())
    points=[]
    for i in range(n):
        x,y=map(int,input().split())
        points.append((x,y))
    points.sort(key= lambda i:(i[0],i[1]))
    s=""
    x,y=0,0
    flag1=0
    for i in points:
        flag=0
        #print(i)
        while(x!=i[0]):
            if i[0]>x:
                x+=1
                s+="R"
            elif i[0]<x:
                flag=1
                break
        while(y!=i[1]):
            if i[1]>y:
                y+=1
                s+="U"
            elif i[1]<y:
                flag=1
                break
            #print(x,y,s)
        s+=(i[0]-x)*'R'+(i[1]-y)*'U'
        x=i[0]
        y=i[1]
        if flag:
            flag1=1
            break
    if flag1:
        print("NO")
    else:
        print("YES")
        print(s)
            
            
        
