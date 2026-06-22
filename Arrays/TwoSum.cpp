#include <bits/stdc++.h>
using namespace std;

vector<int> twoSum(vector<int> &arr, vector<int> &ans, int target)
{
    int n = arr.size();
    unordered_map<int, int> mp;
    for (int i = 0; i < n; i++)
    {
        if (mp.count(target - arr[i]))
        {
            ans[0] = mp[target - arr[i]];
            ans[1] = i;
            break;
        }
        mp[arr[i]] = i;
    }
    return ans;
}

int main()
{
    int arrSize;
    cout << "Enter the Size of Array: ";
    cin >> arrSize;
    vector<int> v(arrSize);
    vector<int> ans(2);
    for (int i = 0; i < arrSize; i++)
    {
        cin >> v[i];
    }
    int k;
    cout << "Enter the target: ";
    cin >> k;
    twoSum(v, ans, k);
    /*cout<<"{ ";
    for(int itr : ans){
        cout<<itr<<" ";
    }
    cout<<"}";*/
    return 0;
}