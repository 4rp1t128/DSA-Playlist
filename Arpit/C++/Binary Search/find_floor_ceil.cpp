#include <bits/stdc++.h>
using namespace std;

class Test{
    public:
        vector<int> getFloorAndCeil(vector<int> nums, int x) {
            vector<int> ans(2, -1);
            int left = 0, right = nums.size() - 1;
            int floor = -1, ceil = -1;
            while(left <= right){
                int mid = left + (right - left) / 2;
                if(nums[mid] == x){
                    floor = nums[mid];
                    ceil = nums[mid];
                    ans[0] = floor;
                    ans[1] = ceil;
                    return ans;
                }else if(nums[mid] < x){
                    floor = nums[mid];
                    ans[0] = floor;
                    left = mid + 1;
                
                }else{
                    ceil = nums[mid];
                    ans[1] = ceil;
                    right = mid - 1;
                }
            }
            return ans;

        }
        void printVecctor(vector<int> ans){
            cout << "Floor: " << ans[0]<<endl;
            cout << "Ceil: " << ans[1]<<endl;
        }
};

int main(){
    vector<int> nums = {1, 2, 8, 10, 10, 12, 19};
    int x = 5;
    Test t;
    vector<int> ans = t.getFloorAndCeil(nums, x);
    t.printVecctor(ans);
    return 0;
}