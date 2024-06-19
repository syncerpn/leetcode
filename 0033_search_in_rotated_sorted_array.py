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