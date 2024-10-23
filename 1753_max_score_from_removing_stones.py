# expanding logic
class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        if a >= b >= c:
            if b + c >= a:
                return (a + b + c) // 2
            else:
                return b + c

        return self.maximumScore(max(a,b,c), a+b+c - max(a,b,c) - min(a,b,c), min(a,b,c))

# and the compact version
class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        return min((a + b + c) // 2, a + b + c - max(a, b, c))