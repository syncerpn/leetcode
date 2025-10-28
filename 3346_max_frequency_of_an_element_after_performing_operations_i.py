# sort + bisect
class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        nums.sort()
        ans = 1
        d = Counter(nums)
        for a in range(max(nums) + 1):
            l = bisect.bisect_left(nums, a-k)
            r = bisect.bisect_right(nums, a+k)
            ans = max(ans, min(d[a] + numOperations, r - l))
        return ans