# its absolute value obviously
class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        m = nums[0]
        for n in nums:
            if abs(n) < abs(m):
                m = n
            elif abs(n) == abs(m) and n > 0:
                m = n
        return m