#include <bits\stdc++.h>
using namespace std;

int findLargest(vector<int> &arr)
{
    int temp = 0;
    for (int i = 0; i < arr.size(); i++)
    {
        if (arr[temp] < arr[i])
        {
            temp = i;
        }
    }
    return temp;
}

int secondLargest(vector<int> &arr)
{
    int temp1 = findLargest(arr);
    arr[temp1] = INT_MIN;
    int temp2 = findLargest(arr);
    return arr[temp2];
}

int secondLargest(vector<int> &arr, int n){
    int first=arr[0],second = INT_MIN;
    for(int itr:arr){
        if(itr>first && itr>second){
            second  = first;
            first = itr;
        }else if(itr<first && itr>second){
            second = itr;
        }
    }
    if(second == INT_MIN) return -1;
    return second;
}

int main()
{
    int n;
    cout << "Enter the Size of an Array : ";
    cin >> n;
    vector<int> v(n, 0);
    for (int i = 0; i < n; i++)
    {
        cin >> v[i];
    }
    //int ans = secondLargest(v);
    int ans = secondLargest(v,n);
    cout << "The Second Largest in an Array: " << ans;
    return 0;
}