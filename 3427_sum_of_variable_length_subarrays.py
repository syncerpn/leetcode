# fairly good problem
# prefix sum
class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        acc = list(accumulate(nums))
        ans = 0
        for i, a in enumerate(nums):
            ans += acc[i]
            s = max(0, i - a) - 1
            if s != -1:
                ans -= acc[s]
        return ans