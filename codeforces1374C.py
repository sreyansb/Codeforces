for _ in range(int(input())):
    n=int(input())
    s=input()
    stack=[]
    front=-1
    numberofsteps=0
    wrongpositions=[]
    for i in range(n):
        if s[i]=='(':
            stack.append('(')
            front+=1
        else:
            if front!=-1 and stack[front]=='(':
                front-=1
            else:
                wrongpositions.append(i)
        #print(stack)
    print(len(wrongpositions))
        
