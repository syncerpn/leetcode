# crazy: greedy solution
# it is just much cleaner than other solutions
class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        proc = []
        ans = m = 0  # m represents max value of finished event so far
        for s,e,v in events:
            proc.append( (s, True, v) )     # time, is_start, val
            proc.append( (e+1, False, v) )  # use e+1 (inclusive)
        proc.sort()  # sort by time
        
        for time, is_start, val in proc:
            if is_start:
                ans = max(ans, m+val)
            else:
                m = max(m, val)
        return ans

# retry with mono stack and binary search
class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort(key=lambda e: (e[1], e[0]))
        h = [(0, 0)]
        ans = 0
        for s, e, v in events:
            if not h or h[-1][1] < v:
                h.append((e, v))
            i = bisect.bisect(h, (s, 0))
            ans = max(ans, h[i-1][1] + v)
        return ans