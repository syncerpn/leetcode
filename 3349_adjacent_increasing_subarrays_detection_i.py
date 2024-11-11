# keep evaluating increasing subarrays
class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        if k == 1:
            return True
        p, q, n = 1, 1, len(nums)
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                q += 1
                if (p >= k and q >= k) or (q >= 2 * k):
                    return True
            else:
                p, q = q, 1
        return False