# knowing it is dp did not help this time, because the constraints do not allow this
# this solution resulted in tle
class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        MOD = 10 ** 9 + 7
        d = [[0] * (maxValue + 1) for _  in range(n+1)]

        d[1] = [1] * (maxValue + 1)

        for k in range(1, n):
            for v in range(1, maxValue+1):
                t = 1
                while t * v <= maxValue:
                    d[k+1][t*v] += d[k][v]
                    d[k+1][t*v] %= MOD
                    t += 1
        
        return sum(d[n]) % MOD

# so go back and think of a more optimized solution
# one of them, suggested by yegao and lee
# we view this problem as changes of array state
# where we start with:
# [1], [2], ..., [maxValue]
# f = {1:1, 2:1, ..., maxValue:1}
# next
# [1, 1], [1, 2], ..., [1, maxValue], [2, 2], [2, 4], ...,
# (now we only need to care about the end of the array in counter)
# f = {1: 1, 2: 2, ...}
# each iteration, we can make a change to array
# and compute how many ways for an array to have a specific value at its end
class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        MOD = 10 ** 9 + 7

        ans = maxValue
        f = {i: 1 for i in range(1, maxValue+1)}

        for k in range(1, n):
            d = Counter()
            for x in f:
                for m in range(2, maxValue//x+1):
                    ans += math.comb(n-1, k) * f[x]
                    d[m*x] += f[x]
            f = d
            ans %= MOD
        
        return ans

# also take a look at "star and bar" problem