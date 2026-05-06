# prefix forward and backward path
class Solution:
    def minCost(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        n = len(nums)
        F = [0, 1]
        for i in range(1, n-1):
            if nums[i+1] - nums[i] < nums[i] - nums[i-1]:
                F.append(F[-1] + 1)
            else:
                F.append(F[-1] + nums[i+1] - nums[i])

        B = [0, 1]
        for i in range(n-2, 0, -1):
            if nums[i+1] - nums[i] < nums[i] - nums[i-1]:
                B.append(B[-1] + nums[i] - nums[i-1])
            else:
                B.append(B[-1] + 1)

        ans = []
        for i, j in queries:
            if i < j:
                ans.append(F[j] - F[i])
            else:
                ans.append(B[~j] - B[~i])
        return ans