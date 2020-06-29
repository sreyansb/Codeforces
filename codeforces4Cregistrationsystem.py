di={}
for i in range(int(input())):
    k=input()
    if k not in di:
        di[k]=0
        print("OK")
    else:
        di[k]+=1
        print(k+str(di[k]))

    
