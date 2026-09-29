"""_summary_
Basically We Insert Each Element at Its Correct Position
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