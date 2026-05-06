# not that easy as its rating shows
# we need to keep track of nums[j] in a mono decreasing stack
# going from right to left
# if nums[i] is higher than the top of the stack
# the stack pops out number to be nums[k] later, as high as possible yet still smaller than nums[i]
# (nums[i] will be nums[j] in the next iteration)
# next iter, if nums[i] < nums[k]
# we know it (and nums[k]) will be smaller than nums[j] in the top of the mono stack
# that is a valid pattern
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        nums_k = -inf
        s = []
        for i in range(n-1, -1, -1):
            a = nums[i]
            if a < nums_k:
                return True
            while s and a > s[-1]:
                nums_k = s.pop()
            s.append(a)
        return False