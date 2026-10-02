# Intuition: This algorithm works with recursion. The whole array is distributed until we get sorted array. It works on divide and conquer approach.

class Solution:
    def merge(self, arr, st_idx, mid, end_idx):
        left_arr=[]
        right_arr=[]

        for i in range(st_idx, mid+1):
            left_arr.append(arr[i])

        for j in range(mid+1, end_idx+1):
            right_arr.append(arr[j])

        left_idx = 0
        right_idx =0
        write_idx =st_idx

        while left_idx<len(left_arr) and right_idx< len(right_arr):
            if right_arr[right_idx]<=left_arr[left_idx]:
                arr[write_idx] = right_arr[right_idx]
                right_idx+=1
            else:
                arr[write_idx] = left_arr[left_idx]
                left_idx+=1

            write_idx+=1

        while left_idx< len(left_arr):
            arr[write_idx] = left_arr[left_idx]
            left_idx+=1
            write_idx+=1

        while right_idx< len(right_arr):
            arr[write_idx] = right_arr[right_idx]
            right_idx+=1
            write_idx+=1


    def merge_sort_helper(self, st_idx, end_idx, arr):
        if st_idx>=end_idx:
            return

        mid = (st_idx+end_idx)//2
        self.merge_sort_helper(st_idx, mid, arr)
        self.merge_sort_helper(mid+1, end_idx, arr)

        self.merge(arr, st_idx, mid, end_idx)

    def merge_sort(self, arr):
        n = len(arr)
        if (n<2):
            return arr

        self.merge_sort_helper(0, n-1, arr)


if __name__ == "__main__":
    arr= [45,12,8,9,5]
    sol = Solution()
    sol.merge_sort(arr)
    print(arr)
  