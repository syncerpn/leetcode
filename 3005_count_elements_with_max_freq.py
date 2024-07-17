# count as usual
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        d = {}
        m = 0
        c = 0
        for n in nums:
            if n not in d:
                d[n] = 0
            d[n] += 1
            if d[n] > m:
                m = d[n]
                c = m
            elif d[n] == m:
                c += m
        return c
