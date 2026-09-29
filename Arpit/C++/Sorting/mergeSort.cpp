#include<bits/stdc++.h>
using namespace std;

void merge(vector<int> &arr,int low,int mid,int high){
    int n1 = mid-low +1;
    int n2 = high - mid;
    vector<int>left(n1);
    vector<int>right(n2);
    for(int i = 0;i<n1;i++){
        left[i] = arr[low+i];
    }
    for(int i = 0; i<n2; i++){
        right[i] = arr[mid+1+i];
    }
    int i =0,j = 0,k=low;
    while(i<n1 && j<n2){
        if(left[i]>right[j]){
            arr[k] = right[j];
            j++;
        }else{
            arr[k] = left[i];
            i++;
        }
        k++;
    }
    while(i<n1){
        arr[k] = left[i];
        i++;
        k++;
    }
    while(j<n2){
        arr[k] = right[j];
        j++;
        k++;
    }
}

void mergeSort(vector<int> &arr,int low,int high){
    if(low>=high) return;
    int mid = (low+high)/2;
    mergeSort(arr,low,mid);
    mergeSort(arr,mid+1,high);
    merge(arr,low,mid,high);
}


int main(){
    vector<int>v;
    //v = {12,2,3,1,32,4,132};
    v = {9,8,7,6,5,4,3,2,1};
   // v = {1, 1, 1};
   int n = v.size();
    mergeSort(v,0,n-1);
    cout << "{ ";
    for (int itr : v)
    {
        cout << itr << " ";
    }
    cout << "}";
    return 0;
}