# keep track of the largest and second largest for comparison
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        k = 0
        m = nums[k]
        p = 0
        for i in range(1, len(nums)):
            n = nums[i]
            if n > m:
                k = i
                p = m
                m = nums[k]
            elif n == m:
                p = m
            elif n > p:
                p = n
        
        return k if m >= 2 * p else -1