n,m,k=map(int,input().split())
question=[]
for i in range(n):
    stri=input()
    question.append(list(stri))

i=0
question1=question.copy()
while(k>0):
    no=question[i].count(".")
    if no>k:
        for j in range(m):
            if k==0:
                break
            else:
                if question[i][j]==".":
                    question[i][j]="X"
                    k-=1
    else:
        k-=no
        for j in range(m):
                if question[i][j]==".":
                    question[i][j]="X"
    i+=1

for i in range(n):
    for j in range(m):
        print(question[i][j],end="")
    print()
    
    
    
