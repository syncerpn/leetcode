# single-pass
# milestone on/off checking
class Solution:
    def captureForts(self, forts: List[int]) -> int:
        a = None
        e = None
        c = 0
        for i, f in enumerate(forts):
            if f == 1:
                a = i
                if e is not None:
                    c = max(c, a - e - 1)
                    e = None
            elif f == -1:
                e = i
                if a is not None:
                    c = max(c, e - a - 1)
                    a = None
        
        return c