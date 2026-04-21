# easy
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        d = Counter(nums)
        ans = 0
        for k in d:
            if d[k] == 1:
                return -1
            if d[k] <= 3:
                ans += 1
            else:
                ans += d[k] // 3 + int(d[k] % 3 > 0)
        return ans