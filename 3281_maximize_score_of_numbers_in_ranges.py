# binary search
# it was a long time since the last time
# so i thought of binary search pretty late during the contest
class Solution:
    def maxPossibleScore(self, start: List[int], d: int) -> int:
        def is_valid(m):
            a = start[0]
            for b in start[1:]:
                if a + m > b + d:
                    return False
                else:
                    a = max(a + m, b)
            return True
                
        start.sort()
        n = len(start)
        l, r = 0, start[-1] - start[0] + d
        while l <= r:
            m = (l + r) // 2
            if is_valid(m):
                l = m+1
            else:
                r = m-1
        return l-1