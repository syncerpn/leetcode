# recursive + mem
class Solution:
    cache = {0: 0, 1: 1}
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        if n in Solution.cache:
            return Solution.cache[n]
        
        r = self.fib(n-1) + self.fib(n-2)
        Solution.cache[n] = r
        return r