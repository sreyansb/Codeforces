#include<stdio.h>
#include<stdlib.h>
#include<string.h>
int main()
{
    char s[100005];
    scanf("%s",s);
    int *a = (int *)calloc(strlen(s)+1,sizeof(int));
    for(int i=1;i<strlen(s);i++)
        {if (s[i]==s[i-1])
        a[i+1]=a[i]+1;
        else
        {
            a[i+1]=a[i];
        }}
    int k;
    scanf("%d",&k);
    while(k--)
    {
        int l,b;
        scanf("%d %d",&l,&b);
        printf("%d\n",a[b]-a[l]);
    }
   
}