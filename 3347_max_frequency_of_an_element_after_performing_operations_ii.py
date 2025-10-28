# just use scheduling + interval
class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        d = {}
        c = Counter(nums)
        for a in nums:
            if a not in d:
                d[a] = 0
            if a - k not in d:
                d[a-k] = 0
            d[a-k] += 1
            if a + k + 1 not in d:
                d[a + k + 1] = 0
            d[a + k + 1] -= 1
        p = 0
        ans = 0
        for a in sorted(d.keys()):
            p += d[a]
            ans = max(ans, min(c[a] + numOperations, p))
        return ans