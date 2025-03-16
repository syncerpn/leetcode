# binary search
# this one caught me offguard
# quote:
# "So when we say nums[mid] > nums[mid+1],
# It means there must be a peak element
# in left side of array (from index 0 to index mid)"
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[mid + 1]:
                r = mid
            else:
                l = mid + 1
        return l
        