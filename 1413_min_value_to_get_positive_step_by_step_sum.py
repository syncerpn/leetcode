# just find min prefix sum
# then make sure that min + target value >= 1
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        m = nums[0]
        s = 0
        for n in nums:
            s += n
            if m > s:
                m = s
        
        return max(1 - m, 1)