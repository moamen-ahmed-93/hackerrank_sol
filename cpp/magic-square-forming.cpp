#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int cost[8]={0};
    int a[3][3]={8,1,6,3,5,7,4,9,2};
    int b[3][3]={4,3,8,9,5,1,2,7,6};
    int c[3][3]={2,9,4,7,5,3,6,1,8};
    int d[3][3]={6,7,2,1,5,9,8,3,4};
    int e[3][3]={6,1,8,7,5,3,2,9,4};
    int f[3][3]={8,3,4,1,5,9,6,7,2};
    int g[3][3]={4,9,2,3,5,7,8,1,6};
    int h[3][3]={2,7,6,9,5,1,4,3,8};
    int rr[3][3];
    for(int i=0;i<3;i++)
        {
        for(int j=0;j<3;j++)
            {
            cin>>rr[i][j];
        }
    }
    //int ca=0,cb=0,cc=0,cd=0,ce=0,cf=0,cg=0,ch=0;
    for(int i=0;i<3;i++)
        {
        for(int j=0;j<3;j++)
            {
            cost[0]+=abs(a[i][j]-rr[i][j]);
            cost[1]+=abs(b[i][j]-rr[i][j]);
            cost[2]+=abs(c[i][j]-rr[i][j]);
            cost[3]+=abs(d[i][j]-rr[i][j]);
            cost[4]+=abs(e[i][j]-rr[i][j]);
            cost[5]+=abs(f[i][j]-rr[i][j]);
            cost[6]+=abs(g[i][j]-rr[i][j]);
            cost[7]+=abs(h[i][j]-rr[i][j]);
        }
    }
    int ca=*min_element(cost,cost+8);
    cout<<ca;
    return 0;
}
