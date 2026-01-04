# sieve of era like
class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        n = max(nums)
        q = int(n ** 0.5) + 1
        dp = [2] * (n + 1)
        dp[1] = 1
        sp = [1 + i for i in range(n + 1)]
        sp[1] = 1
        for i in range(2, q):
            dp[i * i] += 1
            sp[i * i] += i
            j = i + 1
            while i * j <= n:
                dp[i * j] += 2
                sp[i * j] += i + j
                j += 1
        
        return sum(sp[a] for a in nums if dp[a] == 4)