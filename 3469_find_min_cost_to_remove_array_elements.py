# dp solution
# we want to check all possible ways
# with a helper function "solve"
# solve(j, i) where j is the index of remaining element before i
# and i is the starting index of the remaining part
# so that the remaining elements are like
# [ _ _ j _ _ i i+1 i+2 i+3 ...]
# _ being removed elements
class Solution:
    def minCost(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[-1] * (n+1) for _  in range(n+1)]
        def solve(j, i):
            if i == n:
                return nums[j]
            if i == n-1:
                return max(nums[j], nums[i])
            if dp[j][i] == -1:
                f = max(nums[i], nums[i+1]) + solve(j, i+2)
                s = max(nums[j], nums[i+1]) + solve(i, i+2)
                t = max(nums[j], nums[i]) + solve(i+1, i+2)
                
                dp[j][i] = min(f, s, t)
            return dp[j][i]

        return solve(0, 1)

# this one is super fast
# instead of using index, we use value of the previous element
class Solution:
    def minCost(self, nums: List[int]) -> int:
        @lru_cache(maxsize=None)
        def dp(prev: int, i: int) -> int:
            if i + 2 > n:
                return max(prev, *nums[i:]) if i < n else prev
            c, b, a = sorted((nums[i], nums[i+1], prev))
            ans = a + dp(c, i + 2)
            ans = min(ans, b + dp(a, i + 2))
            return ans
            

        n = len(nums)
        if n < 3: return max(nums)
        return dp(nums[0], 1)