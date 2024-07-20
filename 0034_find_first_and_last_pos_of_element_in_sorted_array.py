# pure binary search to achieve O(logn)
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if nums:
            n = len(nums)
            i = bisect_left(nums, target)
            j = bisect_right(nums, target)
            if i < n and nums[i] == target:
                return [i, j-1]

        return [-1, -1]