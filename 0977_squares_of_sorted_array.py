# two-pointer, partition merging to make it O(n)
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums_sq = [0] * len(nums)
        i = 0
        j = n - 1
        k = n - 1
        while i < j:
            if abs(nums[j]) > abs(nums[i]):
                nums_sq[k] = nums[j] ** 2
                j -= 1
            else:
                nums_sq[k] = nums[i] ** 2
                i += 1
            k -= 1
        nums_sq[k] = nums[i] ** 2
        return nums_sq