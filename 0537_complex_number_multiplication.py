# simple string manip
class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        a, b = list(map(int, num1[:-1].split("+")))
        c, d = list(map(int, num2[:-1].split("+")))
        h = a * c - b * d
        k = a * d + b * c
        return f"{h}+{k}i"