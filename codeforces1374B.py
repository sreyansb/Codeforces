for _ in range(int(input())):
    n=int(input())
    numberofsteps=0
    while(n!=1):
        if n%6==0:
            n//=6
            numberofsteps+=1
        elif n%6==3:
            n*=2
            numberofsteps+=1
        else:
            numberofsteps=-1
            break
    print(numberofsteps)
            
