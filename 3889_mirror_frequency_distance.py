# easy
class Solution:
    def mirrorFrequency(self, s: str) -> int:
        A = "abcdefghijklmnopqrstuvwxyz0123456789"
        M = "abcdefghijklmnopqrstuvwxyz"[::-1] + "0123456789"[::-1]
        D = {a: b for a, b in zip(A, M)}
        d = Counter()
        for c in s:
            d[c] += 1
        
        ans = 0
        for c in d:
            if D[c] not in d:
                ans += abs(d[c] - d[D[c]])
            ans += abs(d[c] - d[D[c]])
        return ans // 2