class Solution:
    def reformatNumber(self, number: str) -> str:
        digits = "".join([c for c in number if c != " " and c != "-"])
        n = len(digits)
        if n % 3 == 0:
            return "-".join([digits[3*i:3*i+3] for i in range(n//3)])
        elif n % 3 == 1:
            return "-".join([digits[3*i:3*i+3] for i in range(n//3-1)] + [digits[-4:-2]] + [digits[-2:]])
        else:
            return "-".join([digits[3*i:3*i+3] for i in range(n//3)] + [digits[-2:]])