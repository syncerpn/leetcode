# fairly easy actually
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0
        for i in range(1, len(nums)):
            n = nums[i]
            if l >= 1 and nums[l-1] == n:
                continue
            l += 1
            nums[l] = n
        return l + 1