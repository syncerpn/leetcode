# due to that answering within 10^-5 is accepted
# just return 1 when n > 4800
# otherwise, use dp
# monte-carlo problem?
class Solution:
    def soupServings(self, n: int) -> float:
        if n > 4800: return 1
        @functools.cache
        def f(a, b):
            if a <= 0 and b <= 0: return 0.5
            if a <= 0: return 1
            if b <= 0: return 0
            return 0.25 * (f(a - 4, b) + f(a - 3, b - 1) + f(a - 2, b - 2) + f(a - 1, b - 3))
        n = math.ceil(n / 25.0)
        return f(n, n)
        