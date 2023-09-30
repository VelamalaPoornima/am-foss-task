#include<stdio.h>
int main()
{
    int n,i,count,j;
    printf("enter the number: ");
    scanf("%d",&n);
    printf("prime numbers are: /n");
    for(i=1; i<=n; i++)
    {
        count=0;
        for(j=1; j<=n; j++)
        {
            if(i%j==0)
                count++;
        }
        if(count==2)
            printf("%d \n" ,i);
    }
    return 0;
}