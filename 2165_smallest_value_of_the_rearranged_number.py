# easy
class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0:
            return num
        neg = True if num < 0 else False
        s = str(abs(num))
        z = s.count("0")
        if neg:
            s = "".join(sorted(list(s), reverse=True))
            return -int(s)
        s = "".join(sorted(list(s)))
        s = s[z] + "0" * z + s[z+1:]
        return int(s)