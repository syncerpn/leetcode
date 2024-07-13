# hash map obviously
# actually, pretty good problem
class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        d = {}
        r = 0
        for n in nums:
            if n + k in d:
                r += d[n + k]
            if n - k in d:
                r += d[n - k]
            if n not in d:
                d[n] = 0
            d[n] += 1
        return r