# this is actually two strategies, depending on the length of nums
# if nums has even number of elements, we can force the opponent
# to take either sum of all odd-indexed or sum of all even-indexed numbers in nums
# take whichever is larger
# 2nd, we need dp where dp[j] is the best "score diff" we can get from nums[i:j]
class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        if n % 2 == 0: 
            return True
            
        dp = list(nums)
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                dp[j] = max(nums[i] - dp[j], nums[j] - dp[j - 1])
        return dp[-1] >= 0