# sort and sliding window
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k == 1:
            return 0

        nums.sort()
        d_min = None
        for i in range(len(nums)-k+1):
            a = nums[i]
            b = nums[i+k-1]
            if d_min is None:
                d_min = b - a
            else:
                d_min = min(b - a, d_min)
        
        return d_min
