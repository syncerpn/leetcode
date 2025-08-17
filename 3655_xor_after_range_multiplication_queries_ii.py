# sqrt decomposition
# read and learn and revisit
class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        n = len(nums)
        m = isqrt(n) + 1
        events = defaultdict(lambda: [1] * n)

        for l, r, k, v in queries:
            if k <= m:
                events[k][l] = events[k][l] * v % MOD
                r2 = r + ((l - r) % k or k)
                if r2 < n:
                    events[k][r2] = events[k][r2] * pow(v, MOD - 2, MOD) % MOD
            else:
                for i in range(l, r + 1, k):
                    nums[i] = nums[i] * v % MOD

        for k, row in events.items():
            for i in range(k):
                cur = 1
                for j in range(i, n, k):
                    cur = cur * row[j] % MOD
                    nums[j] = nums[j] * cur % MOD

        ans = 0
        for x in nums:
            ans ^= x
        return ans
        