# fairly good
# needed to think a bit
class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        l = 1
        l_max = -1
        s = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + s:
                l += 1
                l_max = max(l, l_max)
                s = -s
            else:
                if nums[i] == nums[i-1] + 1:
                    s = -1
                    l = 2
                else:
                    s = 1
                    l = 1
        return l_max