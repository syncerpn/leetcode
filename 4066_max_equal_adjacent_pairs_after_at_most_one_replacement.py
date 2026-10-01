# easy
# just check all pairs before replacement
# then choose the pair with most occurence
class Solution:
    def maxEqualAdjacentPairs(self, nums: list[int]) -> int:
        d = {}
        ans = 0
        for a, b in pairwise(nums):
            if a == b:
                ans += 1
            else:
                ab = (a, b) if a < b else (b, a)
                if ab not in d:
                    d[ab] = 0
                d[ab] += 1
        return ans + (max(d.values()) if d else 0)