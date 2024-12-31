# it is getting easier to me
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)

        @functools.cache
        def test(i):
            if i >= n:
                return 0
            return min(costs[0] + test(bisect.bisect_left(days, days[i] + 1)),
                       costs[1] + test(bisect.bisect_left(days, days[i] + 7)),
                       costs[2] + test(bisect.bisect_left(days, days[i] + 30)))
        
        return test(0)