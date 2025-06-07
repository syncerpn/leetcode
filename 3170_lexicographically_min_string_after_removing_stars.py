# fairly easy
class Solution:
    def clearStars(self, s: str) -> str:
        A = "abcdefghijklmnopqrstuvwxyz"
        d = {a: [] for a in A}
        p = [True] * len(s)
        for i, c in enumerate(s):
            if c == "*":
                p[i] = False
                for a in A:
                    if d[a]:
                        p[d[a].pop()] = False
                        break
            else:
                d[c].append(i)
        
        ans = ""
        for i, c in enumerate(s):
            if p[i]:
                ans += c
        return ans