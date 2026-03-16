# easy
class Solution:
    def minCost(self, nums1: list[int], nums2: list[int]) -> int:
        d = Counter(nums1)
        f = d + Counter(nums2)
        ans = 0
        for a in f:
            if f[a] % 2:
                return -1
            ans += abs(f[a] // 2 - d[a])
        return ans // 2