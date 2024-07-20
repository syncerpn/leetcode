# i was very closed to this optimal solution
# just then i realized we need to deal with already-sorted array separately
# the point is, we will build a point from left to right
# that forms a strictly subarray, called left prefix
# and do the similar right to left to form right suffix
# with each of them, we can remove gradually one element + those not belong to the subarray
# for example: [4,6,5,3,7,8,9]
# left is [4,6] and right is [3,7,8,9] (5 does not belong to any)
# with the left, we can remove [5,...,9] to get full the left
# or [6,5,...,9] and [4,6,5,...,9]
# similar thing with the right
# the we bridge left and right into
# [4,9] [4,8,9] [4,7,8,9]
# [4,6,9] [4,6,8,9] [4,6,7,8,9]
# each the 6 above, we remove respectively
# [6,5,3,7,8] [6,5,3,7] [6,5,3]
# [5,3,7,8] [5,3,7] [5,3]
# therefore, just count the formable arrays to get the removable ones
class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        n = len(nums)
        # find left prefix
        l = 0
        while l < n - 1 and nums[l+1] > nums[l]:
            l += 1
        # if the whole array is sorted, we can stop and return the count based on math
        if l == n - 1:
            return n * (n + 1) // 2
        # else, we have to deal with right suffix
        # there is probably subarray from 
        r = n - 1
        while r > 0 and nums[r-1] < nums[r]:
            r -= 1
        
        # then try form sorted array bridging left and right prefix
        # the number of arrays we can form equals to number of incremovable array in between left and right parts
        result = (l + 1) + (n - r) + 1
        for k in range(l+1):
            while r < n and nums[k] >= nums[r]:
                r += 1
            result += n - r
        
        return result