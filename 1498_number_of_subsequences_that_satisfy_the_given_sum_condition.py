# it looks difficult at first
# but actually, all it needs are subsequences
# we can simply first sort the array
# then use two-pointer to find the min and max indices of candidates
# and count it with bitmask
# for example: [3, 5, 6, 7]
# we have one candidate [3, 5, 6]
# 3 must always appear, then 5, 6 can be bitmasked
# 3 x x (3 00)
# 3 x 6 (3 01)
# 3 5 x (3 10)
# 3 5 6 (3 11)
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = 10 ** 9 + 7
        nums.sort()

        n = len(nums)
        j = n - 1
        ans = 0
        for i, a in enumerate(nums):
            while j >= i and nums[j] + a > target:
                j -= 1
            if j >= i:
                ans += 2 ** (j-i)
                ans %= MOD
        return ans

# 2 ** (j-i) deals with large number, thus is very slow
# how about caching it first with dp
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = 10 ** 9 + 7
        nums.sort()

        n = len(nums)
        j = n - 1
        ans = 0
        dp = [1]
        for i, a in enumerate(nums):
            while j >= i and nums[j] + a > target:
                j -= 1
            if j >= i:
                while len(dp) < j - i + 1:
                    dp.append(dp[-1] * 2 % MOD)
                ans += dp[j-i]
                ans %= MOD
        return ans
