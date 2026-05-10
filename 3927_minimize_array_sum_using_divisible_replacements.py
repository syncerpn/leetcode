# sieve
# surprised with complexity that it works with 10^5 constraint lol
class Solution:
    def minArraySum(self, nums: list[int]) -> int:
        m = max(nums)
        d = Counter(nums)
        K = sorted(list(d.keys()))
        ans = 0
        for k in K:
            if k not in d:
                continue
            for p in range(k, m + 1, k):
                if p in d:
                    ans += k * d[p]
                    del d[p]
        return ans