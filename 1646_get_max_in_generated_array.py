# simulate it
# with memoi or dp
# up to you
class Solution:
    cache = {0: 0, 1: 1}
    def getMaximumGenerated(self, n: int) -> int:
        def f(n):
            if n in Solution.cache:
                return Solution.cache[n]
            if n % 2:
                k = f(n//2) + f(n//2+1)
            else:
                k = f(n//2)
            
            Solution.cache[n] = k
            return k
        
        arr = [f(i) for i in range(n+1)]
        return max(arr)