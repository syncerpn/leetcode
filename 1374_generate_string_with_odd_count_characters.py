# simply detach n into sum of odd number
# 1, 1 + o, or 1 + 1 + o
class Solution:
    def generateTheString(self, n: int) -> str:
        if n == 1:
            return "a"
        if n % 2 == 0:
            return "a" + "b" * (n-1)
        return "ab" + "c" * (n-2)