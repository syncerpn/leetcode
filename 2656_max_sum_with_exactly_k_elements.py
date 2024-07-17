# can be solved with math
class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        m = max(nums)
        return k * (2 * m + k - 1) // 2