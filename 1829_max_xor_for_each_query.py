# prefix xor
class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        x = 0
        ans = [0] * len(nums)
        for i, n in enumerate(nums):
            x ^= n
            ans[-1-i] = (1 << maximumBit) - 1 - x
        return ans