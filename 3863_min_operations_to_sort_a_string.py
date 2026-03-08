# just a few cases to consider
class Solution:
    def minOperations(self, s: str) -> int:
        ss = "".join(sorted(s))
        if s == ss:
            return 0
        if len(s) == 2:
            return -1
        
        mi, ma = min(s), max(s)
        if s[0] == mi or s[-1] == ma:
            return 1
        elif ma in s[1:] or mi in s[:-1]:
            return 2
        return 3
