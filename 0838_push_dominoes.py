# stack
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        s = []
        ans = ""
        for i, c in enumerate(dominoes):
            if c != ".":
                s.append((i, c))
        if not s:
            return "." * n
        
        if s[0][1] == "L":
            ans += s[0][0] * "L"
        else:
            ans += s[0][0] * "."
        
        for (i, a), (j, b) in pairwise(s):
            if a == b:
                ans += a * (j-i)
            elif a == "L":
                ans += "L" + "." * (j-i-1)
            else:
                m = (j - i + 1) // 2
                ans += "R" + "R" * (m - 1) + (j - i + 1 - 2 * m) * "." + "L" * (m - 1)
        
        if s[-1][1] == "R":
            ans += "R" * (n - s[-1][0])
        else:
            ans += "L" + "." * (n - s[-1][0] - 1)
        return ans