# with memoi, it is very fast
class Solution:
    cache = {}
    def getKth(self, lo: int, hi: int, k: int) -> int:
        def power(x):
            if x in Solution.cache:
                return Solution.cache[x]
            if x == 1:
                return 0
            Solution.cache[x] = 1 + (power(3*x+1) if x % 2 else power(x>>1))
            return Solution.cache[x]
        return sorted(list(range(lo, hi+1)), key=power)[k-1]