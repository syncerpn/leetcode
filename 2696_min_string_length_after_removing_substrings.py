# stack obviously
class Solution:
    def minLength(self, s: str) -> int:
        t = []
        for c in s:
            if t:
                if (t[-1] == "A" and c == "B") or (t[-1] == "C" and c == "D"):
                    t.pop()
                    continue
            t.append(c)
        return len(t)