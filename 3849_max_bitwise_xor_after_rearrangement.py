# easy
class Solution:
    def maximumXor(self, s: str, t: str) -> str:
        n = len(t)
        z, o = t.count("0"), t.count("1")
        ans = ""
        for c in s:
            if c == "0":
                if o > 0:
                    o -= 1
                    ans += "1"
                else:
                    z -= 1
                    ans += "0"
            else:
                if z > 0:
                    z -= 1
                    ans += "1"
                else:
                    o -= 1
                    ans += "0"
        return ans