"""_summary_
        Question: Given a sorted array of nums consisting of distinct integers
        and a target value, return the index if the target is found. If not, 
        return the index where it would be if it were inserted in order.
"""

from typing import List


def search_insert_position(numbers:List[int], target:int) -> int:
    left = 0 
    right = len(numbers) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if numbers[mid] == target:
            return mid
        elif numbers[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left


def main() -> None:
    numbers = list(map(int, input().split()))
    target = int(input())
    pos = search_insert_position(numbers, target)
    print(pos)


if __name__ == "__main__":
    main()