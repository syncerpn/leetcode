# fairly simple
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        n_min = min(nums)
        n_max = max(nums)
        while n_min:
            n_min, n_max = n_max % n_min, n_min
        return n_max