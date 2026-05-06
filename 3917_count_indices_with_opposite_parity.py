# easy
class Solution:
    def countOppositeParity(self, nums: list[int]) -> list[int]:
        n = len(nums)
        ans = [0] * n
        o, e = 0, 0
        for i in range(n-1, -1, -1):
            if nums[i] % 2:
                ans[i] = e
                o += 1
            else:
                ans[i] = o
                e += 1
        return ans