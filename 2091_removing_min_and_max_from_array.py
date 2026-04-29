# just a few cases
class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        miv, mav = inf, -inf
        mii, mai = -1, -1
        for i, a in enumerate(nums):
            if a < miv:
                miv = a
                mii = i
            if a > mav:
                mav = a
                mai = i
        
        return min(n + 1 + mii - mai, max(mii, mai) + 1, n + 1 - mii + mai, n - min(mii, mai))