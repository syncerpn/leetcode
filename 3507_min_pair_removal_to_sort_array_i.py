# naive method
# just simulate it
class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        def check(A):
            for a, b in pairwise(A):
                if a > b:
                    return False
            return True

        ans = 0
        while not check(nums):
            m, j = float("inf"), 0
            for i, (a, b) in enumerate(pairwise(nums)):
                if m > a + b:
                    m = a + b
                    j = i
            nums.pop(j)
            nums[j] = m
            ans += 1
            
        return ans