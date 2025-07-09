# hash map
# make sure you dont misunderstand the question
# lol
class Solution:
    def sumDigitDifferences(self, nums: List[int]) -> int:
        k = len(str(nums[0]))
        n = len(nums)
        ans = 0
        for i in range(k):
            d = Counter([a // (10 ** i) % 10 for a in nums])
            for b in d:
                ans += d[b] * (n - d[b])
        
        return ans >> 1