# dp in #3335 wont work because of how large t can be
class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        d = {c: i for i, c in enumerate("abcdefghijklmnopqrstuvwxyz")}
        MOD = 10 ** 9 + 7

        dp = [[0] * (t + 1) for _ in range(26)]
        for i in range(26):
            dp[i][0] = 1
    
        for j in range(1, t + 1):
            for i in range(26):
                for k in range(nums[i]):
                    dp[i][j] += dp[(i+1+k) % 26][j-1]
                dp[i][j] %= MOD
        
        ans = 0
        for c in s:
            ans = (ans + dp[d[c]][t]) % MOD
        return ans

# but it is inspiring because we can actually form a matrix transformation
# with the pattern seen in the dp code above
# now that i have to touch "fast pow" algorithm
# which is something new i learned today
# very worthy
# anyway, pure python implementation of matmul is rather slow
# top solutions simply use numpy but no other myths
# also, i put a lot of "% MOD"
# because without doing so may result in tle due to handling large numbers
class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        d = {c: i for i, c in enumerate("abcdefghijklmnopqrstuvwxyz")}
        MOD = 10 ** 9 + 7

        def matmul(x, y):
            z = [[0] * 26 for _ in range(26)]
            for i in range(26):
                for j in range(26):
                    for k in range(26):
                        z[i][j] += (x[i][k] * y[k][j]) % MOD
                        z[i][j] %= MOD
                
            return z

        def matpow(m, p):
            r = [[0] * 26 for _ in range(26)]
            for i in range(26):
                r[i][i] = 1

            while p > 0:
                if p & 1:
                    r = matmul(m, r)
                m = matmul(m, m)
                p >>= 1
            
            return r

        m = [[0] * 26 for _ in range(26)]
        for i in range(26):
            for k in range(nums[i]):
                m[i][(i + 1 + k) % 26] = 1
        
        m = matpow(m, t)
        f = Counter(s)
        
        ans = 0

        for c in f:
            ans = ans + f[c] * sum(m[d[c]])
        return ans % MOD