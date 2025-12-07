# monoqueue + sliding window + prefix sum + dp
# counting part need revisited
class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        MOD = 10 ** 9 + 7
        ma, mi = deque(), deque()
        l = 0
        ans = 0
        n = len(nums)
        dp = [0] * (n + 1)
        ps = [0] * (n + 1)
        dp[0] = 1
        ps[0] = 1
        for r, a in enumerate(nums):
            while ma and nums[ma[-1]] <= a:
                ma.pop()
            ma.append(r)
            while mi and nums[mi[-1]] >= a:
                mi.pop()
            mi.append(r)
            while l < r:
                if nums[ma[0]] - nums[mi[0]] <= k:
                    break
                l += 1
                if ma[0] < l:
                    ma.popleft()
                if mi[0] < l:
                    mi.popleft()
            if l > 0:
                dp[r+1] = (ps[r] - ps[l-1]) % MOD
            else:
                dp[r+1] =  ps[r] % MOD
            ps[r+1] = (ps[r] + dp[r+1]) % MOD

        return dp[n]
