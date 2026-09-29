"""_summary_
        Basically We Select the minimum element and swap it with Elemet 
        in such a way so that smallest Element come to left side of a List
"""



from typing import List

def swap(number:List[int],a,b) -> None:
    number[a],number[b] = number[b],number[a]

def solve(numbers)->None:
    for i in range(len(numbers)):
        min_index = i
        for j in range(i+1,len(numbers)):
            if(numbers[j]<numbers[min_index]):
                min_index = j
        swap(numbers,i,min_index)


def main() -> None:
    numbers = list(map(int, input().split()))
    solve(numbers)
    print(numbers)


if __name__ == "__main__":
    main()