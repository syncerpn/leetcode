# easy
class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        P = {2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97}
        l, r, n = 0, 0, len(nums)
        for i in range(n):
            if nums[i] in P:
                l = i
                break
                
        for i in range(n):
            if nums[~i] in P:
                r = n - 1 - i
                break
        return r - l