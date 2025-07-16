# all odds, all evens, or alternatives
class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        o, e, xo, xe = 0, 0, 0, 0
        for a in nums:
            if a % 2:
                o += 1
                if xe % 2:
                    xe += 1
                if xo % 2 == 0:
                    xo += 1
            else:
                e += 1
                if xe % 2 == 0:
                    xe += 1
                if xo % 2:
                    xo += 1
        return max(o, e, xo, xe)