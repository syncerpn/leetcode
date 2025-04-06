# dp, with tracking
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        dp = [1] * n
        jp = list(range(n))
        m, q = 1, 0
        for i, a in enumerate(nums):
            for j, b in enumerate(nums):
                if j >= i:
                    break
                if a % b == 0:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        jp[i] = j
                        if dp[i] > m:
                            m, q = dp[i], i
        ans = []
        while q != jp[q]:
            ans.append(nums[q])
            q = jp[q]
        ans.append(nums[q])
        return ans