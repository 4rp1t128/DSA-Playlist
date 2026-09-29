"""_summary_
    Basically We Divide the Array into Two Halves and Then Merge Them
"""
from typing import List



def merge(left:List[int], right:List[int]) -> List[int]:
    result = []
    i = j = 0
    while i < len(left)and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result. append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
    

def merge_Sort(numbers: List[int]) -> List[int]:
    if len(numbers) <= 1:
        return numbers
    mid = len(numbers)//2
    left = merge_Sort(numbers[:mid])
    right = merge_Sort(numbers[mid:])

    return merge(left, right)




def main() -> None:
    numbers = list(map(int, input().split()))
    print(merge_Sort(numbers))

if __name__ == "__main__":
    main()