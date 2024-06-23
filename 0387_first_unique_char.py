# single pass, store index of unique char; if not unique, store -1
class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        k = ""
        for i, c in enumerate(s):
            if c not in d:
                d[c] = i
                k += c
            else:
                d[c] = -1
        
        for c in k:
            if d[c] >= 0:
                return d[c]
        
        return -1