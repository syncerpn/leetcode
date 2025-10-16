# count the modulo
class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        d = Counter(a % value for a in nums)
        ans, m = 0, float("inf")
        for k in range(value):
            if d[k] < m:
                ans, m = k, d[k]
        return ans + m * value