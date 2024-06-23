# calculate overlapping between two consecutive time in the series
# no overlapping gives max duration; otherwise, partly
class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        r = 0
        for i, j in pairwise(timeSeries):
            r += min(j-i, duration)
        
        return r + duration