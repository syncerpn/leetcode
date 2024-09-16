# true dp solution
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

# my solution
# but feel like it is similar to the below binary search
# the idea is to keep track of the possibly 1st, 2nd, 3rd, ... element of the subsequence
# everytime we see a number that is smaller than, let's say, i-th element,
# but larger than i-1-th element
# we can use replace the i-th element with that number
# because it allows more chance to add future numbers into the subsequence
# e.g. 5 8 6 7
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [nums[0]]
        for i in range(1, len(nums)):
            n = nums[i]
            if n > dp[-1]:
                dp.append(n)
            else:
                j = len(dp) - 1
                while j > 0:
                    if dp[j] > n > dp[j-1]:
                        dp[j] = n
                        break
                    j -= 1
                else:
                    if dp[0] > n:
                        dp[0] = n
        return len(dp)

# the binary search solution mentioned
# same idea
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []
        for n in nums:
            if not dp or dp[-1] < n:
                dp.append(n)
            else:
                j = bisect.bisect_left(dp, n)
                dp[j] = n
        return len(dp)