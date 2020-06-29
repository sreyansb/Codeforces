for _ in range(int(input())):
    h,m=map(int,input().split())
    time=h*60+m
    difftime=1440-time
    print(difftime)
