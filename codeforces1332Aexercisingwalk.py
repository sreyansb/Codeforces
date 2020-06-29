for _ in range(int(input())):
    a,b,c,d=map(int,input().split())
    x,y,x1,y1,x2,y2=map(int,input().split())
    diffxs=x2-x1+1#represents number of points along x axis
    diffys=y2-y1+1#represents number of points along y axis
    if a+b-x<=diffxs and c+d-y<=diffys:
        print("Yes")
    else:
        print("No")
        
    
    
    
