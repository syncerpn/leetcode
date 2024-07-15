# count and divide
class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        d = {}
        for c in s:
            if c not in d:
                d[c] = 0
            d[c] += 1
        
        t = {}
        for c in target:
            if c not in d:
                d[c] = 0
            if c not in t:
                t[c] = 0
            t[c] += 1
        
        return min([d[c] // t[c] for c in t])