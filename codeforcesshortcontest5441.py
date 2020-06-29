l=input().split(":")
k=input().split(":")
h1=int(l[0])
m1=int(l[1])
h2=int(k[0])
m2=int(k[1])
tavg=((h1+h2)*60+(m1+m2))//2
if tavg//60>9:
    if tavg%60>9:
        tf=str(tavg//60)+":"+str(tavg%60)
    else:
        tf=str(tavg//60)+":0"+str(tavg%60)
else:
    if tavg%60>9:
        tf="0"+str(tavg//60)+":"+str(tavg%60)
    else:
        tf="0"+str(tavg//60)+":0"+str(tavg%60)
print(tf)
