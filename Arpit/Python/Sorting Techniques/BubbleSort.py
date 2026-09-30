"""_summary_
        Basically We Compare Adjacent Elements and Swap them if they are in Wrong Order 
        in sucha way that the largest element bubbles up to the end of the array in each 
        iteration.We try to do this for all the Elements in the Array and 
        Repeat the Process for n-1 Times.
"""

from typing import List

def swap(number: List[int],a:int,b:int) -> None:
    number[a], number[b] = number[b], number[a]

def solve(numbers: List[int]) -> None:
    for i in range(len(numbers)):
        for j in range(0, len(numbers) - i - 1):
            if(numbers[j] > numbers[j + 1]):
                swap(numbers, j, j + 1)


def main()->None:
    numbers = list(map(int,input().split()))
    solve(numbers)
    print(numbers)

if __name__ == "__main__":
    main()