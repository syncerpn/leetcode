# binary search
# that init value of r fucked me up a bit
class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        def is_valid(m):
            h = mountainHeight
            for t in workerTimes:
                h -= int(((m * 8 / t + 1) ** 0.5 - 1) / 2)
                if h <= 0:
                    return True
            return False
        
        l, r = 1, mountainHeight * (mountainHeight + 1) * max(workerTimes) // 2
        while l < r:
            m = (l + r) // 2
            if is_valid(m):
                r = m
            else:
                l = m + 1
        return r