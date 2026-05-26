# easy
class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        d = defaultdict(int)
        ans = []
        for a in nums:
            d[a] += 1
            if d[a] <= k:
                ans.append(a)
        return ans