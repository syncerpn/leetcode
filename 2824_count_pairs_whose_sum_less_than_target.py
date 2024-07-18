# sort + binary search making it O(nlogn)
class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        c = 0
        for i in range(1, len(nums)):
            k = bisect_left(nums[:i], target - nums[i])
            c += k
        return c
