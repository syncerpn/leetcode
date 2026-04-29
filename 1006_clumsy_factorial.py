# easy stack
class Solution:
    def clumsy(self, n: int) -> int:
        OPS = "*/+-"
        i = 0
        s = [n]
        for a in range(n-1, 0, -1):
            if OPS[i] == "*":
                s[-1] *= a
            elif OPS[i] == "/":
                s[-1] //= a
            elif OPS[i] == "+":
                s.append(a)
            elif OPS[i] == "-":
                s.append(a)
            i = (i + 1) % 4
        
        return sum([a if i % 2 or i == 0 else -a for i, a in enumerate(s)])