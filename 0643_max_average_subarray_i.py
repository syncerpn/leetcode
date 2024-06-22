# sliding window should work
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        s = 0
        s_max = None
        for i in range(len(nums)):
            if i < k:
                s += nums[i]
                continue
            if s_max is None:
                s_max = s
            elif s > s_max:
                s_max = s
            s = s - nums[i-k] + nums[i]
        
        if s_max is None:
            s_max = s
        elif s > s_max:
            s_max = s
        return s_max / k