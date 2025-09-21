# easy
class Solution:
    def evenNumberBitwiseORs(self, nums: List[int]) -> int:
        ans = 0
        for a in nums:
            if a % 2 == 0:
                ans |= a
        return ans