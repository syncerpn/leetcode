# find the pivot
# from beginning up to pivot should be sorted
# and from pivot to the cyclic first should be sorted
class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        n = len(nums)
        r = 0
        for i in range(n-1):
            j = i + 1
            if nums[j] < nums[i]:
                r = i
                break
        else:
            return 0
        
        for i in range(r+1, n):
            j = (i+1) % n
            if nums[j] < nums[i]:
                return -1
        
        return n-1-r