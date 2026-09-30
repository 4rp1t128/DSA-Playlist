"""_summary_
        Question: Given a sorted array nums and an integer x. 
        Find the floor and ceil of x in nums. The floor of x is the 
        largest element in the array which is smaller than or equal to x. 
        The ceiling of x is the smallest element in the array greater than or equal to x. 
        If no floor or ceil exists, output -1.
"""

from typing import List

from numpy import number

def find_floor_ceil(numbers:List[int], x : int) -> tuple:
    left = 0
    right = len(numbers) - 1
    floor = -1
    ceil = -1
    while(left <= right):
        mid = left + (right - left) // 2
        if numbers[mid] == x:
            floor = numbers[mid]
            ceil = numbers[mid]
            return floor, ceil
        elif numbers[mid] < x:
            floor = numbers[mid]
            left = mid + 1
        else:
            ceil = numbers[mid]
            right = mid - 1
    return floor, ceil





def main() -> None:
    numbers = list(map(int, input().split()))
    x = int(input())
    floor, ceil = find_floor_ceil(numbers, x)
    print(floor, ceil)



if __name__ == "__main__":
    main()