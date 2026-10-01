"""_summary_
        Ques:
        Given two numbers N and M, find the Nth root of M. The Nth root of a number M 
        is defined as a number X such that when X is raised to the power of N, it equals M. 
        If the Nth root is not an integer, return -1.
    """

def nth_root(N:int, M:int) -> int:
    if M == 0 or M == 1:
        return M
    left = 1
    right = M
    while(left <= right):
        mid = left + (right - left) // 2
        power = 1
        for _ in range(N):
            power *= mid
            if power > M:
                break
        if power == M:
            return mid
        elif power < M:
            left = mid + 1
        else:
            right = mid - 1
    return -1

if __name__ == "__main__":
    N = int(input())
    M = int(input())
    print(nth_root(N, M))