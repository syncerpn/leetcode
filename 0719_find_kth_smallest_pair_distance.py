# binary search
# similar to prime fraction problem #0786
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        def is_valid(m):
            c = 0
            j = 0
            for i in range(n):
                while j < n and nums[j] - nums[i] <= m:
                    j += 1
                c += j - i - 1
            return c < k
            
        nums.sort()
        n = len(nums)

        l = 0
        r = nums[-1] - nums[0]

        while l < r:
            m = (l + r) // 2
            if is_valid(m):
                l = m + 1
            else:
                r = m
        return l