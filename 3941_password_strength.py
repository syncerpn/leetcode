# easy
class Solution:
    def passwordStrength(self, password: str) -> int:
        L = set("abcdefghijklmnopqrstuvwxyz")
        U = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        D = set("0123456789")
        S = set("!@#$")
        password = set(password)
        ans = 0
        for c in password:
            if c in L:
                ans += 1
            elif c in U:
                ans += 2
            elif c in D:
                ans += 3
            elif c in S:
                ans += 5
        return ans
