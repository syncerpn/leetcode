# just a few cases
class Solution:
    def minFlips(self, s: str) -> int:
        o, z = s.count("1"), s.count("0")

        if o < 2 or z == 0:
            return 0
        if o == 2:
            if s[0] == "0" or s[-1] == "0":
                return 1
            return 0
        ans = min(z, o - 1)
        if s[0] == "1" and s[-1] == "1":
            ans = min(ans, o - 2)
        
        return ans