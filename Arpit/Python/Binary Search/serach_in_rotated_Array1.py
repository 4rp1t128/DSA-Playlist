"""_summary_
    Ques: There is an integer array nums sorted in ascending order (with distinct values).
        Prior to being passed to your function, nums is possibly left rotated at an unknown
        index k (1 <= k < nums.length) such that the resulting array is 
        [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). 
        For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices and become 
        [4,5,6,7,0,1,2].Given the array nums after the possible rotation and an integer 
        target, return the index of target if it is in nums, or -1 if it is not in nums.
        You must write an algorithm with O(log n) runtime complexity.
"""
from typing import List


def search_in_rotated_array(numbers:List[int], target : int) -> int:
    left = 0
    right = len(numbers) - 1
    while(left <= right):
        mid = left + (right - left) // 2
        if numbers[mid] == target:
            return mid
        if numbers[left] <= numbers[mid]:
            if numbers[left] <= target < numbers[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if numbers[mid] < target <= numbers[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1


def main() -> None:
    numbers = list(map(int, input().split()))
    target = int(input())
    print(search_in_rotated_array(numbers, target))

if __name__ == "__main__":
    main()

