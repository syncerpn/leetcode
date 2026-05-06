# easy
class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        A = " abcdefghijklmnopqrstuvwxyz"
        d = {a:i+1 for i, a in enumerate("abcdefghijklmnopqrstuvwxyz")}
        ans = []
        while k != n:
            m = min(k - (n-1), 26)
            ans.append(A[m])
            k -= m
            n -= 1
        return "a" * n + "".join(ans[::-1])

# or math
class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        z, mid = divmod(k - n, 25)
        return ('a' * (n - z - 1) + chr(ord('a')+mid) if z < n else '') + 'z' * z