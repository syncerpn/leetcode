# math
# need revisited
# also, this is a simple solution, but not optimal
# should check out other solutions as well
class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        MOD = 10**9 + 7
        return m * pow(m-1, n-k-1, MOD) * comb(n-1, k) % MOD