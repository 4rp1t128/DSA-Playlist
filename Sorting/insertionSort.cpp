#include <bits/stdc++.h>
using namespace std;

void insertionSort(vector<int> &arr){
    int n = arr.size();
    for(int i =0; i<n;i++){
        int j = i;
        while(j>0 && arr[j]<arr[j-1]){
            swap(arr[j-1],arr[j]);
            j--;
        }
    }
}

int main()
{
    vector<int>v;
    v = {12,2,3,1,32,4,132};
    //v = {9,8,7,6,5,4,3,2,1};
    // v = {1, 1, 1};
    insertionSort(v);
    cout << "{ ";
    for (int itr : v)
    {
        cout << itr << " ";
    }
    cout << "}";
 return 0;
}