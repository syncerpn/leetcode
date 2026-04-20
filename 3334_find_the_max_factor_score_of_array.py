# O(n) solution with prefix and suffix gcd lcm
class Solution:
    def maxScore(self, nums: List[int]) -> int:
        def incremental(index_order):
            darr, marr = [0] * n, [0] * n
            d, m = 0, 1
            for i in index_order:
                d = gcd(d, nums[i])
                m = lcm(m, nums[i])
                darr[i], marr[i] = d, m
            return darr, marr

        n = len(nums)
        dpre, mpre = incremental(range(n))
        dsuf, msuf = incremental(reversed(range(n)))
        res = dpre[-1] * mpre[-1]
        for i in range(n):
            d1, d2 = dpre[i - 1] if i > 0 else 0, dsuf[i + 1] if i + 1 < n else 0
            m1, m2 = mpre[i - 1] if i > 0 else 1, msuf[i + 1] if i + 1 < n else 1
            res = max(res, gcd(d1, d2) * lcm(m1, m2))
        return res