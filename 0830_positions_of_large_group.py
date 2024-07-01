# one-pass checking
class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        if len(s) < 3:
            return []
        k = 0
        r = []
        for i in range(1, len(s)):
            if s[i] != s[k]:
                if i - k >= 3:
                    r.append([k, i-1])
                k = i
        
        if i - k + 1 >= 3:
            r.append([k, i])
        return r