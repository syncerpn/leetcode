# easy with counter and counting
class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        ans = n * (n-1) // 2
        d = Counter([a - i for i, a in enumerate(nums)])
        return ans - sum(d[i] * (d[i] - 1) // 2 for i in d)