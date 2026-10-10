"""_summary_
        Ques:
        Given an array nums of size n, which denotes the positions of stalls, and an integer k, 
        which denotes the number of aggressive cows, assign stalls to k cows such that the minimum 
        distance between any two cows is the maximum possible. Find the maximum possible minimum distance.
    """
from typing import List
class Solution:
    def aggressiveCows(self, nums:List[int], k:int)-> int :
        nums.sort()
        left = 1
        right = nums[-1] - nums[0] # last stall position - first stall position
        while(left <= right):
            mid = left + (right -left) // 2
            if(self.isPossible(nums, k ,mid)):
                left = mid + 1
            else:
                right = mid
        return right


    def isPossible(self, nums:List[int], k:int, mid:int)-> bool:
        cows_placed = 1
        last_pos = nums[0]
        for i in range(1, len(nums)):
            if(nums[i] - last_pos >= mid):
                cows_placed += 1
                last_pos = nums[i]
                if(cows_placed >= k):
                    return True
        return False

    def main() -> None:
        nums = list(map(int, input().split()))
        k = int(input())
        solution = Solution()
        max_min_distance = solution.aggressiveCows(nums, k)
        print(max_min_distance)