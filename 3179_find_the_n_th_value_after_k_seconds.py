# isnt it pascal's triangle
class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        MOD = 10 ** 9 + 7
        return math.comb(k+n-1, n-1) % MOD

# make sure it O(min(n, k))
class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        MOD = 10 ** 9 + 7
        ans = 1
        for i in range(min(k, n-1)):
            ans = ans * (k+n-1-i) // (i+1)

        return ans % MOD