# with math for faster compute O(1)
class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:
        MOD = 10 ** 9 + 7
        h = target // 2
        p = min(h, n)
        ans = p * (p + 1) // 2
        if h < n:
            ans += (target + target + n - h - 1) * (n - h) // 2
        return ans % MOD
        