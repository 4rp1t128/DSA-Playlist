# Intuition: Find the smallest element in the unsorted array and swap it with the first element of the unsorted array. Repeat this process for the remaining unsorted array.

# [45, 55, 13, 9, 12]
# Iter1: [45, 55, 13, 9, 12]  ---->  [9, 55. 13, 45, 12] ( 45 compared with 55 - 45 smaller, 45 compared with 13 - 13 smaller, 13 compared with 9 - 9 smaller, 9 compared with 12 - 9 smaller, hence replaced with index of assumed minimum value)
# Iter2: [9, 55. 13, 45, 12]  ---->  [9,12, 13, 45, 55] (Unsorted array starts from 55 : 55 compared with 13 - 13 smaller, 13 compared with 45 - 13 smaller, 13 compared with 12 - 12 smaller, hence 12 swapped with 55 )
# Iter3: [9, 12, 13, 45, 55]  -----> (Elements are already in position, No swapping is required)

class Solution:
    def selection_sort(self, arr):
        n= len(arr)
        for index in range(n-1):
            least_val_idx = index
            for current in range(index+1, n):
                if arr[current]< arr[least_val_idx]:
                    least_val_idx = current
            arr[index], arr[least_val_idx] = arr[least_val_idx], arr[index]
        return arr


if __name__ == "__main__":
    arr = list(map(int, input("Enter the numbers separated by spaces: ").split()))
    solution = Solution()
    solution.selection_sort(arr)
    print("Sorted Array is", arr)
