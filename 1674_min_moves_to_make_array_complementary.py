# need revisit
class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        diff = [0] * (2 * limit + 2)
        for i in range(n // 2):
            a, b = sorted([nums[i], nums[n - 1 - i]])
            diff[2] += 2
            diff[2 * limit + 1] -= 2
            diff[a + 1] -= 1
            diff[b + limit + 1] += 1
            diff[a + b] -= 1
            diff[a + b + 1] += 1
        ans, c = n, 0
        for i in range(2, 2 * limit + 1):
            c += diff[i]
            ans = min(ans, c)
        return ans