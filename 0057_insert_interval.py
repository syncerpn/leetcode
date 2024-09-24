# monostack
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        s = [newInterval]
        for a, b in intervals:
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