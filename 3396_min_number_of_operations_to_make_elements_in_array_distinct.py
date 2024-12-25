# easy
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        v = set()
        n = len(nums)
        for i in range(n-1, -1, -1):
            a = nums[i]
            if a in v:
                return i // 3 + 1
            v.add(a)
        return 0