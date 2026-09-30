"""_summary_
Basically We Insert Each Element at Its Correct Position by Comparing 
It With the Previous Elements and Shifting Them to the Right if They Are Greater
 Than the Current Element.
"""

def solve(numbers) -> None:
    for i in range(1, len(numbers)):
        key = numbers[i]
        j = i - 1
        while j >= 0 and key < numbers[j]:
            numbers[j+1] = numbers[j]
            j -= 1
            numbers[j + 1] = key
        

def main() -> None:
    numbers = list(map(int,input().split()))
    solve(numbers)
    print(numbers)

if __name__ == "__main__":
    main()