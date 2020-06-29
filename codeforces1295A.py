for i in range(int(input())):
    n=int(input())
    if n%2:
        print("7"+"1"*(int((n-3)/2)))
    else:
        print("1"*(n//2))
    
    
