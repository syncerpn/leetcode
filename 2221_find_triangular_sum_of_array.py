# using comb to find pascal triangle coeffs
# this is math, yet trivial way
class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums)
        return sum(ni * comb(n-1, i) for i, ni in enumerate(nums)) % 10

# this is much much more beautiful with math proof
# copied from others
class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        result = 0
        m = len(nums) - 1
        mCk = 1
        for k, num in enumerate(nums):
            result = (result + mCk * num) % 10
            mCk *= m - k
            mCk //= k + 1
        return result