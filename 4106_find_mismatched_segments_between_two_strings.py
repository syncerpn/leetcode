# easy
class Solution:
    def findMismatchedSegments(self, s1: str, s2: str) -> list[list[str]]:
        p, q = [], []
        ans = []
        for a, b in zip(s1, s2):
            if a != b:
                p.append(a)
                q.append(b)
            else:
                if p:
                    ans.append(["".join(p), "".join(q)])
                    p, q = [], []
        if p:
            ans.append(["".join(p), "".join(q)])
        return ans