# easy
class Solution:
    def minimumCost(self, nums: list[int], k: int) -> int:
        MOD = 10 ** 9 + 7
        ans = 0
        b = k
        for a in nums:
            if b < a:
                m = int(math.ceil((a - b) / k))
                ans += m
                b += k * m
            b -= a
        return ans * (ans + 1) // 2 % MOD

# a better math
class Solution:
    def minimumCost(self, nums: list[int], k: int) -> int:
        MOD = 10 ** 9 + 7
        ans = int(math.ceil(sum(nums) / k)) - 1
        return ans * (ans + 1) // 2 % MOD