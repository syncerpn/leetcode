# sliding window
# fairly simple
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        if len(s2) < n:
            return False
        
        d = {c: 0 for c in "abcdefghijklmnopqrstuvwxyz"}
        for c in s1:
            d[c] += 1

        s = set([k for k in d if d[k]])
        for i, c in enumerate(s2):
            if i >= n:
                l = s2[i-n]
                d[l] += 1
                if d[l]:
                    s.add(l)
                else:
                    s.discard(l)
            d[c] -= 1
            if d[c]:
                s.add(c)
            else:
                s.discard(c)
            
            if not s:
                return True
        return False