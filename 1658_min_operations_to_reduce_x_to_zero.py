# pretty easy
class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        P = {0: 0}
        p = 0
        n = len(nums)
        for i in range(n):
            a = nums[i]
            p += a
            if p > x:
                break
            if p not in P:
                P[p] = i + 1
        
        ans = inf if x not in P else P[x]
        for i in range(n-1, -1, -1):
            x -= nums[i]
            if x < 0:
                break
            if x in P:
                ans = min(ans, n - i + P[x])
        return ans if ans <= n else -1