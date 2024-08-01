# use flipping boolean check to avoid simulation
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        f = True
        ans = 0
        for n in nums:
            if (f and n == 0) or (not f and n == 1):
                f = not f
                ans += 1
        return ans