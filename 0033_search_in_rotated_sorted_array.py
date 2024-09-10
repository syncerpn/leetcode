class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # you can break the problem into binary search for the pivot point
        # then binary search within either half of the array
        # or use this solution which combines both procedure
        n = len(nums)
        l = 0
        r = n - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            # if left half array is sorted
            if nums[l] <= nums[m]:
                # and target is within the range
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            # if right half is sorted
            else:
                # and target is within the range
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return -1

# or we can find the min pivot first
# then also use binary for the two halves of the array
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[r] < nums[m]:
                l = m + 1
            else:
                r = m
        if r > 0:
            t = bisect.bisect_left(nums, target, hi=r)
            if t < r and nums[t] == target:
                return t
        if r < len(nums):
            t = bisect.bisect_left(nums, target, lo=r)
            if t < len(nums) and nums[t] == target:
                return t
        return -1