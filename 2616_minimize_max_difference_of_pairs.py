# pretty nice problem for practicing binary search
# again, we use binary search because any solution is easy to validate, yet finding a strategy is not easy
class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        def is_valid(m):
            i = 0
            pm = p
            while pm > 0:
                if i > len(nums) - 2:
                    break
                if nums[i+1] - nums[i] <= m:
                    i += 1
                    pm -= 1
                i += 1

            return pm == 0

        if len(nums) == 1:
            return 0
        nums.sort()
        l = 0
        r = nums[-1] - nums[0]
        while l < r:
            m = (l + r) // 2
            if is_valid(m):
                r = m
            else:
                l = m + 1
        return r

