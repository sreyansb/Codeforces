for _ in range(int(input())):
    n=int(input())
    if n&3!=0:
        print("NO")
    else:
        print("YES")
        soln=[0]*(n)
        sumi=0
        number=2
        sumofnumbers=0
        for i in range(n//2):
            soln[i]=number
            soln[i+n//2]=number-1
            sumi+=1
            number+=2
        soln[n-1]=sum(soln[:n//2])-sum(soln[n//2:n-1])
        print(*soln)
            
