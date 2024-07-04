# count the freq
# then keep going back and forth and back and forth
class Solution:
    def sortString(self, s: str) -> str:
        d = {}
        for c in s:
            if c not in d:
                d[c] = 0
            d[c] += 1

        v = sorted(d.keys())

        r = ""
        c = 0
        n = len(s)
        m = len(v)
        i = 0
        j = 1
        while c < n:
            ki = v[i]
            if d[ki] > 0:
                r += ki
                d[ki] -= 1
                c += 1
            
            i += j
            if i == m:
                j = -1
                i = m-1
            elif i == -1:
                j = 1
                i = 0
        
        return r