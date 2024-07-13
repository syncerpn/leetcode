# track necessary nums
class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        f_min, s_min, s_max, f_max = sorted(nums[:4])
        for n in nums[4:]:
            if n > f_max:
                f_max, s_max = n, f_max
            elif n > s_max:
                s_max = n
            elif n < f_min:
                f_min, s_min = n, f_min
            elif n < s_min:
                s_min = n
        return s_max * f_max - f_min * s_min