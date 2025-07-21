# etho prime
class Solution:
    def splitArray(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return sum(nums)
        
        v = set([0, 1])
        ans = nums[0] + nums[1]

        for i in range(2, n):
            if i in v:
                continue
            ans -= nums[i]
            for j in range(2*i, n, i):
                if j in v:
                    continue
                v.add(j)
                ans += nums[j]
        return abs(ans)