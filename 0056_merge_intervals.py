# sorting and monostack
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        s = []
        for a, b in intervals:
            if not s:
                s.append([a, b])
                continue
            c, d = s[-1]
            if d < a:
                s.append([a, b])
            elif b < c:
                s.pop()
                s.append([a, b])
                s.append([c, d])
            else:
                s.pop()
                s.append([min(a, c), max(b, d)])
        return s