# boil down to combination
# does not matter left or right
# just pick to get a total of k visible people
class Solution:
    def countVisiblePeople(self, n: int, pos: int, k: int) -> int:
        MOD = 10 ** 9 + 7
        return 2 * math.comb(n-1, k) % MOD

# without python's lib
# we may have to implement it using fermat's theorem (probably?)
# here is a nice one
class Solution:
    def countVisiblePeople(self, n: int, pos: int, k: int) -> int:
        MOD = 10 ** 9 + 7
        k = min(k, n - 1 - k)
        div = factorial(k) % MOD
        cur = div
        for i in range(k + 1, n - k):
            cur = (cur * i) % MOD
        div = (div * cur) % MOD
        div = pow(div, MOD - 2, MOD)
        for i in range(n - k, n):
            cur = (cur * i) % MOD
        return 2 * (cur * div) % MOD