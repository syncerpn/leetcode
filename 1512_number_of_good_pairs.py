# using hash map should give O(n) time and space
# also, we can achieve the result with single-pass
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        d = {}
        c = 0
        for n in nums:
            if n not in d:
                d[n] = 0
            d[n] += 1
            c += d[n] - 1
        return c