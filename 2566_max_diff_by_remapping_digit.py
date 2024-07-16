# min can be obtained by replacing first digit with 0
# max can be obtained by replacing first not-9 digit with 9
class Solution:
    def minMaxDifference(self, num: int) -> int:
        s = str(num)
        a = s
        for c in s:
            if c != "9":
                a = s.replace(c, "9")
                break
        b = s.replace(s[0], "0")
        return int(a) - int(b)
