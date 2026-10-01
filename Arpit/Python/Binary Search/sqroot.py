"""_summary_
        Ques:
        Given a non-negative integer x, return the square root of x 
        rounded down to the nearest integer. The returned integer should be non-negative 
        as well.You must not use any built-in exponent function or operator.
        For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
    """

def sqroot(x:int) -> int:
    if x == 0 or x == 1:
        return x
    ans = 0
    left = 1
    right = x
    while left <= right:
        mid = left + (right - left) // 2
        if (mid == x // mid):
            return mid
        elif(mid < x//mid):
            left = mid + 1
            ans = mid
        else:
            right = mid - 1
    return ans

if __name__ == "__main__":
    x = int(input())
    print(sqroot(x))    