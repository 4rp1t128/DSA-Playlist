#include<bits\stdc++.h>
using namespace std;

int findLargest(vector<int> &arr){
    int temp = INT_MIN;
    for(int itr : arr){
        if(temp<itr){
            temp = itr;
        }
    }
    return temp;
}

int main(){
    int n ;
    vector<int>arr;
    cout<<"Enter the Size of Array: ";
    cin>>n;
    cout<<"Enter the Element of Array"<<endl;
    for(int i =0 ; i< n; i++){
        int ele;
        cin>>ele;
        arr.push_back(ele);
    }
    int ans = findLargest(arr);
    cout<<"the Largest Element of An Array: "<<ans;

    return 0;
}