# binary search
# to validate m
# if m is valid
# the total time consumed should be m * n
# each battery may consume at most m
# so we need to check whether the total amount of contribution >= m * n
class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        l, r = min(batteries), sum(batteries) // n
        while l <= r:
            m = (l + r) // 2
            k = 0
            for a in batteries:
                k += min(a, m)
            if k >= m * n:
                l = m + 1
            else:
                r = m - 1
        return l - 1
