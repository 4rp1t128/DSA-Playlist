#include <bits\stdc++.h>
using namespace std;

int maxLengthSubarrayWithSumK(vector<int> &arr, int n, int k)
{
    int curSum = 0, maxSubArrayLength = 0;
    unordered_map<int, int> mp;

    for (int i = 0; i < n; i++)
    {
        curSum += arr[i];
        if (curSum == k)
        {
            maxSubArrayLength = max(maxSubArrayLength, i + 1);
        }
        else if (mp.count(curSum - k))
        {
            maxSubArrayLength = max(maxSubArrayLength, i - mp[curSum - k]);
        }
        mp[curSum] = i;
    }

    return maxSubArrayLength;
}

int main()
{
    int arrSize, k;
    cout << "Enter the Size of Array: ";
    cin >> arrSize;
    vector<int> arr(arrSize);
    for (int i = 0; i < arrSize; i++)
    {
        cin >> arr[i];
    }
    cout << "Enter the sum of Sub-Array: ";
    cin >> k;
    int ans = maxLengthSubarrayWithSumK(arr, arrSize, k);
    cout << "Longest Length of Sub-Array with " << k << " Sum: " << ans;
    return 0;
}