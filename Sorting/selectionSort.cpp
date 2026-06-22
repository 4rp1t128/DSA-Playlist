#include <bits/stdc++.h>
using namespace std;

vector<int> selectionSort(vector<int> a)
{
    int n = a.size();
    for (int i = 0; i < n - 1; i++)
    {
        int temp = i;
        for (int j = i + 1; j < n; j++)
        {
            if (a[j] < a[temp])
            {
                temp = j;
            }
        }
        swap(a[i], a[temp]);
    }
    return a;
}

int main()
{
    vector<int> v;
    vector<int> ans;
    v = {12,2,3,1,32,4,123};

    ans = selectionSort(v);
    cout << "{ ";
    for (int itr : ans)
    {
        cout << itr << " ";
    }
    cout << "}";
    return 0;
}