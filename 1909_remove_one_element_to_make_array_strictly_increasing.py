# this should be a hard problem to find O(n) solution
# so we need two condition
class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        c = 0
        for i in range(1, len(nums)):
            if nums[i-1] >= nums[i]:
                c += 1
                if c >= 2:
                    return False
                if i > 1 and nums[i-2] >= nums[i]:
                    # simulate removal of element
                    # by shifting previous numbers forward
                    nums[i] = nums[i-1]
                # one more shift, but may not necessary in case of exactly one remove
                nums[i-1] = nums[i-2]
        
        return True