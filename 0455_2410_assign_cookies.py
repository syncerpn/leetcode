# try to satisfy low greedy children as many as possible
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        c = 0
        g.sort()
        s.sort()
        i  = 0
        j  = 0
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                c += 1
                i += 1
            j += 1
        
        return c