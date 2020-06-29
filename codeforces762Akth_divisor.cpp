#include <bits/stdc++.h>
#define ll long long
using namespace std;  
int main()
{
    ll n,x;
    set <ll> a;
    cin>>n>>x;
    for(ll i=1;i<=sqrt(n);i++)
    if (n%i==0)
    a.insert({i,n/i});
    if (x<=a.size())
    cout<<*next(a.begin(),x-1);
    else
    {
        cout<<-1;
    }
    return 0;    
}
