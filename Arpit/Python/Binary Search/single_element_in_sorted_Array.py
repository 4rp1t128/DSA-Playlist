"""_summary_
        Ques: You are given a sorted array consisting of only integers where every element appears exactly twice, 
        except for one element which appears exactly once. Return the single element that appears only once. 
        Your solution must run in O(log n) time and O(1) space.
    """
from typing import List

def single_element_in_sorted_array(numbers: List[int]) -> int:
    left = 0
    right = len(numbers) - 1

    while left < right:
        mid = left + (right - left) // 2

        if mid % 2 == 1:
            mid -= 1

        if numbers[mid] == numbers[mid + 1]:
            left = mid + 2
        else:
            right = mid

    return numbers[left]

def main() -> None:
    numbers = list(map(int, input().split()))
    print(single_element_in_sorted_array(numbers))



if __name__ == "__main__":
    main()