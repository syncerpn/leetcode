# we need two zero-ending elements in nums
class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        c = 0
        for n in nums:
            if n & 1 == 0:
                c += 1
                if c == 2:
                    return True
        return False