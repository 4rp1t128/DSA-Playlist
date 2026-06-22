#include <bits/stdc++.h>
using namespace std;

int partition(vector<int> &arr, int low, int high)
{
    int i = low, j = high;
    int pivot = arr[low];
    while (i < j)
    {
        while (arr[i] <= pivot && i <= high - 1)
        {
            i++;
        }
        while (arr[j] > pivot && j >= low + 1)
        {
            j--;
        }
        if (i < j)
        {
            swap(arr[i], arr[j]);
        }
    }
    swap(arr[low], arr[j]); // place the pivot element to its right position
    return j;               // index of the pivot element
}

void quickSort(vector<int> &arr, int low, int high)
{
    if (low >= high)
        return;
    int pivotIndex = partition(arr, low, high);
    quickSort(arr, low, pivotIndex - 1);
    quickSort(arr, pivotIndex + 1, high);
}

int main()
{
    vector<int> v;
    v = {12, 2, 3, 1, 32, 4, 132};
    // v = {9,8,7,6,5,4,3,2,1};
    // v = {1, 1, 1};
    int n = v.size();
    quickSort(v, 0, n - 1);
    cout << "{ ";
    for (int itr : v)
    {
        cout << itr << " ";
    }
    cout << "}";
    return 0;
}