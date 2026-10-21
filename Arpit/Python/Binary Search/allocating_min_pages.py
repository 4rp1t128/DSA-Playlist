class Solution:
    
    def isPossible(self, arr, k, mid):
        curr_page = arr[0]
        stu_count = 1
        for i in range(1,len(arr)):
            if(arr[i]+ curr_page > mid):
                stu_count +=1
                curr_page = arr[i]
                if(stu_count > k):
                    return False
            else:
                curr_page += arr[i]
        return stu_count <= k
    
    
    def findPages(self, arr, k):
        left = max(arr)
        right = sum(arr)
        ans = -1
        if(k <= 0 or len(arr) == 0 or k > len(arr)):
            return ans
        while(left <= right):
            mid = left + (right - left)//2
            if(self.isPossible(arr, k, mid)):
                right = mid - 1
                ans = mid
            else:
                left = mid + 1
        return ans
        
def main():
    arr = list(map(int, input().split()))
    k = int(input())
    solution = Solution()
    min_pages = solution.findPages(arr, k)
    print(min_pages)
