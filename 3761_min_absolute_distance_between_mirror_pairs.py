# easy
class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        @functools.cache
        def r(a):
            b = 0
            while a > 0:
                b = b * 10 + a % 10
                a //= 10
            return b

        d = {}
        n = len(nums)
        ans = n
        for i, a in enumerate(nums):
            b = r(a)
            if a in d:
                ans = min(ans, i - d[a])
            d[b] = i
        return -1 if ans == n else ans