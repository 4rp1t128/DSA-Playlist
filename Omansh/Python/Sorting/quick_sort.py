# Intuition: 
#  Steps: Pick a Pivot and place it on the correct position, smaller on the left and larger on the right.
# All the steps followed after placing a pivot element are similar only. Hence can be solved by recursion as the same process follows and new pivot element will be discovered.
# New arrays will not be formed like merge sort and we will be using pointers to play around.

# Pseudocode:

class Solution:
    def partition_idx(self, arr, st_idx, end_idx):
        left = st_idx
        right = end_idx

        pivot = arr[st_idx]

        while True:
            while (arr[left] <= pivot and left < right):
                left +=1

            while(arr[right]>= pivot and right>=left):
                right-=1

            if left < right:
                arr[left], arr[right] = arr[right], arr[left]
            else:
                break


        arr[right], arr[st_idx] = arr[st_idx], arr[right]
        return right

    def merge_sort(self, arr, st_idx, end_idx):
        if st_idx >= end_idx:
            return

        pt_idx = self.partition_idx(arr, st_idx, end_idx)
        self.merge_sort(arr, st_idx, pt_idx-1)
        self.merge_sort(arr, pt_idx+1, end_idx)

if __name__ == "__main__":
    arr = [10,25, 12, 28, 25, 16 ]
    n= len(arr)
    obj = Solution()
    obj.merge_sort(arr, 0, n-1)
    print(arr)