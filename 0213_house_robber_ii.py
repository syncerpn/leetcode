# we may assume four cases instead of two in the previous problem
# whether we rob (first_y_*) or skip the first house (first_n_*)
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)

        first_n_prev_y = nums[1]
        first_n_prev_n = 0
        first_y_prev_n = nums[0]
        first_y_prev_y = nums[0]
        for n in nums[2:-1]:
            first_n_prev_n, first_n_prev_y = first_n_prev_y, max(first_n_prev_y, first_n_prev_n + n)
            first_y_prev_n, first_y_prev_y = first_y_prev_y, max(first_y_prev_y, first_y_prev_n + n)
        
        n = nums[-1]
        first_n_prev_n, first_n_prev_y = first_n_prev_y, max(first_n_prev_y, first_n_prev_n + n)
        return max(first_n_prev_y, first_n_prev_n, first_y_prev_n, first_y_prev_y)

# same idea but written using the previous problem
class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob_1(nums):
            dp_0 = dp_1 = 0
            for n in nums:
                dp_0, dp_1 = dp_1, max(dp_1, dp_0 + n)
            return max(dp_0, dp_1)
        return max(rob_1(nums[1:]), nums[0] + rob_1(nums[2:-1]))
