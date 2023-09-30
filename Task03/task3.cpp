#include<iostream>
using namespace std;
int main()
{
    int n,i,count,j;
    cout << "enter the number: ";
    cin >> n;
    cout<< "prime numbers are: /n";
    for(i=1; i<=n; i++)
    {
        count=0;
        for(j=1; j<=n; j++)
        {
            if(i%j==0)
                count++;
        }
        if(count==2)
           cout << i << "/n";
    }
    return 0;
}