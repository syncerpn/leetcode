# fairly simple
# would you rob the last house if possible?
class Solution:
    def rob(self, nums: List[int], colors: List[int]) -> int:
        dp_y = 0
        last = None
        dp_n = 0
        for c, a in zip(colors, nums):
            dp_y_next = dp_n + a
            if c != last:
                dp_y_next = max(dp_y_next, dp_y + a)
            last = c
            dp_n_next = max(dp_y, dp_n)
            dp_y, dp_n = dp_y_next, dp_n_next
        return max(dp_y, dp_n)