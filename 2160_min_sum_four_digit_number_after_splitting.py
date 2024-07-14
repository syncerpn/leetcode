# form two nums greedily with two smallest digits leading the two numbers
class Solution:
    def minimumSum(self, num: int) -> int:
        s = sorted(str(num))
        return int(s[1]+s[3]) + int(s[0]+s[2])
        