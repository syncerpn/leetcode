# try flip all negative numbers from the smallest one (largest abs)
# if k > 0, keep flipping the smallest one, which is now positive or zero
class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        i = 0
        while k > 0 and i < len(nums):
            if nums[i] >= 0:
                break
            nums[i] = -nums[i]
            i += 1
            k -= 1
        
        m = nums[i-1]
        if i < len(nums):
            m = min(m, nums[i])
        return sum(nums) - 2 * (k % 2) * m