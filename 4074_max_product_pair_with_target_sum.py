# easy
class Solution:
    def maxProductPair(self, nums: list[int], target: int) -> list[int]:
        d = {}
        m = -inf
        ans = [-1, -1]
        for i, a in enumerate(nums):
            b = target - a
            if b != a and b in d and m < a * b:
                m = a * b
                if a > b:
                    ans = [i, d[b]]
                else:
                    ans = [d[b], i]
            d[a] = i
        return ans