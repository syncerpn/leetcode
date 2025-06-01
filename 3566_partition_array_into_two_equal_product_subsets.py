# bitmasking
class Solution:
    def checkEqualPartitions(self, nums: List[int], target: int) -> bool:
        m = 1
        for a in nums:
            if target % a != 0:
                return False
            m *= a
        
        if m != target * target:
            return False
        n = len(nums)
        def dfs(t, i):
            if t == 1:
                return True
            if i == n:
                return False
            return dfs(t // nums[i], i+1) or dfs(t, i+1)
        
        return dfs(target, 0)