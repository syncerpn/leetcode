# it needs to be even, lol
class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        d = {}
        m = -1
        for n in nums:
            if n % 2:
                continue
            if n not in d:
                d[n] = 0
            d[n] += 1
            if m == -1 or d[n] > d[m] or (d[n] == d[m] and n < m):
                m = n
        return m