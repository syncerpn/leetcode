# O(N2) approach using two pointers to iterate over all triplets
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        res = nums[0] + nums[1] + nums[2]
        d = target - res
        i = 0
        while i < len(nums) - 2:
            l = i + 1
            r = len(nums) - 1
            while l < r:
                tmp = nums[i] + nums[l] + nums[r]
                if tmp == target:
                    return target
                if abs(target-tmp) < abs(target-res):
                    res = tmp
                if tmp > target:
                    r -= 1
                else:
                    l += 1
            i += 1
        return res