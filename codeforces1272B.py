for _ in range(int(input())):
    s=input()
    a=min(s.count('L'),s.count('R'))
    b=min(s.count('U'),s.count('D'))
    final=2*(a+b)
    fstr=a*'L'+b*'D'+a*'R'+b*'U'
    if a ==0 and b!=0:
        final=2
        fstr='UD'
    elif a!=0 and b==0:
        final=2
        fstr='LR'
    print(final)
    print(fstr)
