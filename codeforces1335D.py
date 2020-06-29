for _ in range(int(input())):
    graph=[0]*9
    soln=[0]*9
    for i in range(9):
        graph[i]=input()
        soln[i]=list(graph[i])
        if i==0:
            soln[i][0]=graph[i][1]
        elif i==1:
            soln[i][3]=graph[i][4]
        elif i==2:
            soln[i][6]=graph[i][7]
        elif i==3:
            soln[i][1]=graph[i][2]
        elif i==4:
            soln[i][4]=graph[i][5]
        elif i==5:
            soln[i][7]=graph[i][8]
        elif i==6:
            soln[i][2]=graph[i][1]
        elif i==7:
            soln[i][5]=graph[i][4]
        elif i==8:
            soln[i][8]=graph[i][7]
    for i in range(9):
        soln[i]="".join(soln[i])
        print(soln[i])
        
        
            
            
            
            
            
    
