#include<stdio.h>
int maxpos(long int *a,int n)
{
    long int max=a[0];int pos=0;int i=0;
    while(i<n)
        {if (max<a[i])
            {
                max=a[i];
                pos=i;
            }
        ++i;}
    return pos;
}
int isSorted(long int *a,int n)
{
    int i=1;
    while(i<n)
        {if (a[i-1]>a[i])
            return 0;
        ++i;}
    return 1;
}
//is wrong because: assume 3 variables  3 and 1 are swapped.1 and 2 are then swapped. But essentially only 3 and 1 have been swapped.
int numberofswaps(long int *a,int n)
{int nof=0;
    while(!isSorted(a,n))
    {int pos=maxpos(a,n);
    if (pos!=n-1){
        long int temp=a[pos];
        a[pos]=a[n-1];
        a[n-1]=temp;
        ++nof;
    }
    --n;
    }
    return nof;
}
int main()
{
    int n;
    long int arr[100005];
    scanf("%d",&n);
    for(int i=0;i<n;i++)
        scanf("%ld",&arr[i]);
    if (isSorted(arr,n))
        printf("YES\n");
    else 
	{if (numberofswaps(arr,n)<=1)
        printf("YES\n");
    else
        printf("NO\n");}
    return 0;
}
