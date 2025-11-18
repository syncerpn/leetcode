# same as previous problem
class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        d = {}
        ans = float("inf")
        for i, a in enumerate(nums):
            if a not in d:
                d[a] = []
            d[a].append(i)
            if len(d[a]) >= 3:
                ans = min(ans, 2 * (d[a][-1] - d[a][-3]))
        return ans if ans != float("inf") else -1
        