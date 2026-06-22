#include <bits/stdc++.h>
using namespace std;

bool isSortedRotated(vector<int> &arr)
{
    int n = arr.size();
    int cnt = 0;
    for (int i = 0; i < n; i++)
    {
        if (arr[i] > arr[(i + 1) % n])
        {
            cnt++;
        }
        if (cnt > 1)
            return false;
    }
    return true;
}

int main()
{
    vector<int> v;
   // v = {2, 1, 3, 4};
    //v = {1,2,3,4,5};
    v={3,4,5,1,2};
    bool ans = isSortedRotated(v);
    cout <<ans;
    return 0;
}