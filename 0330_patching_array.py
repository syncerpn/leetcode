# very good problem
# we need to keep track of the next missing value of the currently covered range
# then either accepting a number in the array or patching
# this solution is pretty much clean and optimized
class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        missing = 1
        i = 0
        n_patches = 0

        while missing <= n:
            if i < len(nums):
                if nums[i] <= missing:
                    missing += nums[i]
                    i += 1
                    continue
            # need to patch to cover the missing value
            n_patches += 1
            missing += missing
        return n_patches