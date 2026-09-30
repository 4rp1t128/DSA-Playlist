"""_summary_
        ques:
        There is an integer array nums sorted in non-decreasing order 
        (not necessarily with distinct values).Before being passed to your function, 
        nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the 
        resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]
        (0-indexed). For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and 
        become [4,5,6,6,7,0,1,2,4,4].Given the array nums after the rotation and an integer 
        target, return true if target is in nums, or false if it is not in nums.
        You must decrease the overall operation steps as much as possible.
    """
from typing import List

def search_in_rotated_array2(numbers:List[int], target : int) -> bool:
    left = 0
    right = len(numbers) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if (numbers[mid] == target):
            return True
        if(numbers[left] == numbers[mid] and numbers[right] == numbers[mid]):
            left += 1
            right -= 1
        elif numbers[left] <= numbers[mid]:
            if numbers[left] <= target < numbers[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if numbers[mid] < numbers[right]:
                if numbers[mid] < target <= numbers[right]:
                    left = mid + 1
                else:
                    right = mid - 1
    return False


def main() -> None:
    numbers = list(map(int, input().split()))
    target = int(input())
    print(search_in_rotated_array2(numbers, target))

if __name__ == "__main__":
    main()