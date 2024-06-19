# share the idea with #0033
# in this one, because nums may contain duplicated values, we should eliminate either left tail or right tail
# make sure #0033 is applied on the new array such that its leftmost and rightmost are different
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        for i in range(n-1):
            if nums[i] != nums[-1]:
                break
        else:
            return target == nums[0]
        
        l = i
        r = n - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return True
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
        return False