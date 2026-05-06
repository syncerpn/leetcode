# easy
class Solution:
    def smallestString(self, s: str) -> str:
        A = "abcdefghijklmnopqrstuvwxyz"
        d = {A[i]: A[i-1] for i in range(len(A))}
        l, r = None, None
        for i, c in enumerate(s):
            if c != "a":
                if l is None:
                    l, r = i, i + 1
                else:
                    r = i + 1
            else:
                if l is not None:
                    break
        
        if l is None:
            return s[:-1] + "z"
        p = ""
        for i in range(l, r):
            p += d[s[i]]
        return s[:l] + p + s[r:]