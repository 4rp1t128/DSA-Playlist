"""Quick sort using a pivot and recursive sorting.

We do not write a separate partition function here; the logic stays inside
quickSort and works by splitting the list into smaller, equal, and larger values.
"""
from typing import List


def quickSort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    smaller = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    larger = [x for x in arr if x > pivot]

    return quickSort(smaller) + equal + quickSort(larger)


def main() -> None:
    arr = list(map(int, input().split()))
    print(quickSort(arr))


if __name__ == "__main__":
    main()
