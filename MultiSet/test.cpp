#include <bits/stdc++.h>
using namespace std;

int main()
{
    multiset<int,greater<int>> ms = {5,4,2,4,5,1,2};
    for(auto itr : ms){
        cout<<itr<<" ";
    }
 return 0;
}