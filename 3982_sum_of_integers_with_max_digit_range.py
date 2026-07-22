# easy
class Solution:
    def maxDigitRange(self, nums: list[int]) -> int:
        def digit_range(a):
            ma, mi = 0, 9
            while a > 0:
                d = a % 10
                ma = max(ma, d)
                mi = min(mi, d)
                a //= 10
            return ma - mi

        q = 0
        ans = 0
        for a in nums:
            p = digit_range(a)
            if p > q:
                q = p
                ans = a
            elif p == q:
                ans += a
        return ans