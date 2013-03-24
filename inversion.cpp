#include<iostream>
#include<vector>
#include<cstdio>
using namespace std;
vector<int> a;
long long ret;

void merge(int lb , int mid , int ub)
{
    int add = 0;
    int lp = lb;
    int rp = mid + 1;
    vector<int> temp;
    while( add <= ub - lb + 1 )
    {
        if( lp > mid )
            temp.push_back( a[rp++] );
        else if( rp > ub )
        {
            temp.push_back( a[lp++] );
            ret += ub - mid ;
        }  
        else if( a[lp] < a[rp] )
        {
            temp.push_back( a[lp++] );
            ret += rp - mid - 1;
        }
        else
            temp.push_back( a[rp++] );

        add++;
    }
    for(int i = lb ; i <= ub ; i++)
        a[i] = temp[i-lb];

}

void merge_sort( int lb , int ub )
{
    if( lb >= ub )
        return ;

    int mid = (lb + ub)/2;
    merge_sort(lb , mid);
    merge_sort(mid+1,ub);
    merge( lb , mid , ub );
}


long long inversions()
{
    ret = 0;  
    merge_sort( 0 , a.size() - 1 );
    return ret;
}

int main()
{
    int n;
    scanf("%d", &n);
    a.clear();
    a.resize(n);
    for(int i = 0 ; i < n ; i++)
        scanf("%d", &a[i]);
    cout<<inversions()<<endl;    
    return 0;  
}
