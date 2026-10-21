"""_summary_
        Ques:
        A conveyor belt has packages that must be shipped from one port to another within 
        days days.The ith package on the conveyor belt has a weight of weights[i]. 
        Each day, we load the ship with packages on the conveyor belt (in the order given by weights). 
        We may not load more weight than the maximum weight capacity of the ship.Return the least weight 
        capacity of the ship that will result in all the packages on the conveyor belt being shipped within 
        days days.
    """
from typing import List

class Solution:
    def isPossible(weights:List[int], days:int, min_weight:int) -> bool:
        current_load = 0
        required_days = 1
        for weight in weights:
            if((current_load + weight) > min_weight):
                required_days += 1
                current_load = weight
            else:
                current_load += weight
        return required_days <= days

    def ship_capacity(weights:List[int], days:int) -> int:
        left = max(weights)
        right = sum(weights)
        while(left < right):
            mid = left + (right - left) // 2
            if(Solution.isPossible(weights, days, mid)):
                right = mid
            else:
                left = mid + 1
        return left
    
def main() -> None:
    weights = list(map(int, input().split()))
    days = int(input())
    s = Solution()
    print(s.ship_capacity(weights, days))
