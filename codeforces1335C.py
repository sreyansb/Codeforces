for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    if n==1:
        print(0)
    else:
        di={}
        for i in a:
            if i not in di:
                di[i]=0
            di[i]+=1
        maxi=1
        for i in di:
            maxi=max(di[i],maxi)
        individual_solutions=len(set(a))
        if maxi>individual_solutions:
            print(individual_solutions)
        elif maxi==individual_solutions:
            print(individual_solutions-1)
        else:
            print(maxi)
            
    
        
    
