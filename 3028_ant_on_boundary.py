# prefix sum
class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        p = 0
        c = 0
        for n in nums:
            p += n
            if p == 0:
                c += 1
        return c