#include <bits\stdc++.h>
using namespace std;

void bubbleSort(vector<int> &arr)
{
    int n = arr.size();
    for (int i = 0; i < n - 1; i++)
    {
        for (int j = 0; j < n - i - 1; j++)
        {
            if (arr[j] > arr[j + 1])
            {
                swap(arr[j], arr[j + 1]);
            }
        }
    }
}

int main()
{
    vector<int> v;
    //v = {12,2,3,1,32,4,132};
    v = {9,8,7,6,5,4,3,2,1};
    // v = {1, 1, 1};
    bubbleSort(v);
    cout << "{ ";
    for (int itr : v)
    {
        cout << itr << " ";
    }
    cout << "}";
    return 0;
}