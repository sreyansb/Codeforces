x,y=map(int,input().split())
n=int(input())
"""import cmath
r1=complex(0.5,(3**0.5)/2)
r2=complex(0.5,-(3**0.5)/2)
a2=(complex(y-x*(3**0.5)/2,x/2))/(complex(-1.5,-(3**0.5)/2))
a1=x*0.5*complex(1,3**0.5)-a2*complex(-0.5,-(3**0.5)/2)
print(((a1*r1**n)+a2*(r2**n)).real)
"""
a=[x,y,y-x,-x,-y,x-y]
print(a[(n-1)%6]%1000000007)
