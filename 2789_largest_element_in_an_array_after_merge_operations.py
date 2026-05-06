# backward merge
class Solution:
    def maxArrayValue(self, nums: List[int]) -> int:
        s = []
        for i in range(len(nums)-1, -1, -1):
            if not s or s[-1] < nums[i]:
                s.append(nums[i])
            else:
                s[-1] += nums[i]
        return max(s)