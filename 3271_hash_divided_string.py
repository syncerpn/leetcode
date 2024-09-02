# medium but is actually easy
class Solution:
    def stringHash(self, s: str, k: int) -> str:
        A = {c: i for i, c in enumerate("abcdefghijklmnopqrstuvwxyz")}
        K = {i: c for i, c in enumerate("abcdefghijklmnopqrstuvwxyz")}
        n = len(s)
        ans = ""
        for i in range(0, n, k):
            r = s[i:i+k]
            t = 0
            for c in r:
                t += A[c]
            ans += K[t % 26]

        return ans