#include <bits/stdc++.h>
using namespace std;
 
#define IOS ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);
#define endl "\n"
#define int long long int

const int N = 1e5 + 5;
const int ep=1e9+7;
int a[N];

int32_t main()
{
	IOS;
	int n,k;
    cin>>n>>k;
    a[0]=1;
    for (int i=1;i<=N;++i)
    {
        if (i<k)
            {a[i]=a[i-1];}
        else
        	a[i]=((a[i-1])%ep+(a[i-k])%ep)%ep;
    }
    for (int i=1;i<=N;++i)
        {a[i]=(a[i]+a[i-1])%ep;}
    int l,r;
    while(n--)
    {
        cin>>l>>r;
        cout<<((a[r]-a[l-1])%ep+ep)%ep<<endl;
    }
}
