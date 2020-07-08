for _ in range(int(input())):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    hashmap={}
    number=0
    for i in a:
        if i%k not in hashmap:
            hashmap[i%k]=0
        hashmap[i%k]+=1
    for i in hashmap:
        if i!=0:
            number=max(number,k-i+(hashmap[i]-1)*k)
    if number:
        print(number+1)
    else:
        print(0)
    #complicated it
    #right idea wrong implementation
    '''
    for i in a:
            if i%k==0:
                continue
            if number<k-i%k:
                number=k-i%k
                hashmap[i%k]=1
            elif number==k-i%k and hashmap[i%k]==1:
                number+=k
            elif number==k-i%k and hashmap[i%k]==0:
                hashmap[i%k]=1
            #print(number)
            else:
                if hashmap[i%k]==1:
                    number+=k
            print(number)
    print(number+1)
    '''   
    
    
        
