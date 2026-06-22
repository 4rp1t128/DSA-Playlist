#include <bits\stdc++.h>
using namespace std;

void reverse(vector<int> &a, int low, int high)
{
    while (low < high)
    {
        swap(a[low], a[high]);
        low++;
        high--;
    }
}

void leftRotatedByKTimes(vector<int> &a, int k)
{
    int n = a.size();
    reverse(a, 0, k-1);
    reverse(a, k, n-1);
    reverse(a, 0, n-1);
}

int main()
{
    cout << "Enter the size of an Array: ";
    int n;
    cin >> n;
    vector<int> arr(n);
    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }
    int k;
    cout << "Enter the amount you want to rotate: ";
    cin >> k;
    leftRotatedByKTimes(arr, k);
    cout << "{ ";
    for (int itr : arr)
    {
        cout << itr << " ";
    }
    cout << "}";
    return 0;
}