#include <bits/stdc++.h>
using namespace std;
int main()
{	
	int z,o;
	cin>>z>>o;
	if (o<z-1 || o>(2*z+2))
		cout<<-1<<"\n";
	else
	{
		if (z-1==o)
		{
			cout<<0;
			for(int i=0;i<o;i++)
				cout<<"10";
			cout<<"\n";
		}
		else if (o-1==z)
		{
			cout<<1;
			for(int i=0;i<z;i++)
				cout<<"01";
			cout<<"\n";
		}
		else{
		
		while(o>0&&z>0)
		{if (o<2*z)
		{
			cout<<"10";
			o--;z--;
		}
		else
		{
			cout<<"110";
			o-=2;
			z--;
		}}
		for (int i=0;i<o;i++)
		cout<<1;
		cout<<"\n";
	}}
    return 0;
}
