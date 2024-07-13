# really just O(n2)
# i was overthinking
class Solution:
    def countTriples(self, n: int) -> int:
        r = 0
        for a in range(3, n):
            sqa = a * a
            for b in range(a+1, n):
                sqc = sqa + b * b
                c = int(sqc ** 0.5)
                if c > n:
                    break
                r += 2 if c * c == sqc else 0
        
        return r