# Intuition: Compare adjacent elements and swap them if they are in the wrong order. Repeat this process for the entire array until no swaps are needed, which means the array is sorted.
class Solution:
    def bubble_sort(self, arr):
        n = len(arr)

        for index in range(n-1):
            swapped = False
            for current in range(n-1-index):
                if arr[current] > arr[current+1]:
                    arr[current], arr[current+1] = arr[current+1], arr[current]
                    swapped = True
            if not swapped:
                break

if __name__ == "__main__":
    arr = list(map(int, input("Enter the numbers separated by spaces: ").split()))
    solution = Solution()
    solution.bubble_sort(arr)
    print("Sorted array is:", arr)
