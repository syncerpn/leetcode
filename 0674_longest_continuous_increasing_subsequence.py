class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        l = 1
        l_max = 1
        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                if l_max < l:
                    l_max = l
                l = 1
            else:
                l += 1
        
        if l_max < l:
            l_max = l
        return l_max
        